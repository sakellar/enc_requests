import json
import sys
from collections import Counter
from parser import Parser
from format_output import FormatOutput
import requests


class RequestBuilder:
    """Builds uri for specific arguments"""
    def __init__(self, since, until):
        self.uri = "https://api.stackexchange.com/"
        self.version = "2.2/"
        self.pagesize = "pagesize=20"
        self.answers = "answers?"
        self.questions = "questions/"
        self.from_date = "&fromdate="
        self.since = str(since)
        self.to_date = "&todate="
        self.until = str(until)
        self.order_desc = "&order=desc"
        self.sort = "&sort=activity"
        self.site = "&site=stackoverflow"
        self.answer_filter = "&filter=!40nvjHTUxmmwZk05W"
        self.question_filter = "&filter=!--KJ7Yfz(k3H"

    def get_answer_uri(self):
        """Builds uri for StackOverflow answer"""
        uri_list = list()
        uri_list.append(self.uri)
        uri_list.append(self.version)
        uri_list.append(self.answers)
        uri_list.append(self.pagesize)
        uri_list.append(self.from_date)
        uri_list.append(self.since)
        uri_list.append(self.to_date)
        uri_list.append(self.until)
        uri_list.append(self.order_desc)
        uri_list.append(self.sort)
        uri_list.append(self.site)
        uri_list.append(self.answer_filter)
        return "".join(uri_list)

    def get_question_uri(self, question_id):
        """Builds uri for StackOverflow question"""
        uri_list = list()
        uri_list.append(self.uri)
        uri_list.append(self.version)
        uri_list.append(self.questions)
        uri_list.append(str(question_id)+"?")
        uri_list.append(self.order_desc[1:])
        uri_list.append(self.sort)
        uri_list.append(self.site)
        uri_list.append(self.question_filter)
        return "".join(uri_list)

def get_response_from_stackexchange(uri):
    """Wrapper on requests.get"""
    response = None
    try:
        response = requests.get(uri)
        if int(response.status_code) == 200:
            return response.text
        else:
            raise Exception
    except Exception:
        print "Error in GET request"
        return None

class Collector:
    """MainModule class which collects statistics and parses report"""

    def __init__(self, args):
        self.parser = Parser(args)
        self.since = self.parser.since
        self.until = self.parser.until
        self.format = self.parser.format
        self.answer = None
        self.results = dict()

    def get_stackexchange_data(self):
        """Populates self.answer attribute by GET request text from answers stackoverflow"""
        self.answer = get_response_from_stackexchange(RequestBuilder(self.since,
                                                                     self.until).get_answer_uri())

    def parse_answer_count(self, question_id):
        """Get request on questions uri and parsing of answer_count attribute"""
        response_text = get_response_from_stackexchange(RequestBuilder(self.since,
                                                                       self.until).get_question_uri(question_id))

        try:
            if response_text != None:
                answer_count_json = json.loads(response_text)
                answer_count = int(answer_count_json['items'][0]['answer_count'])
                return answer_count
        except:
            print "Error in parsing answer count response"
            return None

    def collect_statistics(self):
        """
        Collects statistics
        """
        try:
            cnt = Counter()
            cnt_comment = Counter()
            accepted_counter = 0
            total_score = 0.0
            quest_answer_count_total = 0.0
            item_counter = 0
            # Create json
            items = json.loads(self.answer)["items"]
            for item in items:
                item_counter += 1
                if item['is_accepted'] == True:
                    accepted_counter += 1
                    total_score += int(item['score'])
                    question_id = item['question_id']
                answer_count = self.parse_answer_count(item['question_id'])
                if answer_count == None:
                    raise Exception
                quest_answer_count_total += answer_count
                cnt[item['answer_id']] = int(item['score'])
                comment_count = 0
                if item.has_key('comments'):
                    comment_count = len(item['comments'])
                    cnt_comment[item['answer_id']] = comment_count
                comment_count = 0

            self.results['total_accepted_answers'] = int(accepted_counter)
            self.results['accepted_answers_average_score'] = total_score/accepted_counter
            self.results['average_answers_per_question'] = quest_answer_count_total/item_counter

            self.results['top_ten_answers_comment_count'] = dict()
            for item in cnt.most_common(10):
                self.results['top_ten_answers_comment_count'][item[0]] = cnt_comment[item[0]]
        except Exception as e:
            print "Error in parsing data"
            print e

    def produce_report(self):
        """
        Main function for producing report
        """
        fo = FormatOutput(self.results, self.format)
        fo.produce_and_print_report()

def main():
    try:
        collector = Collector(sys.argv[1:])
        collector.get_stackexchange_data()
        collector.collect_statistics()
        collector.produce_report()
    except Exception as e:
        print "Exception in main occured"
        print e

if __name__ == "__main__":
    main()
