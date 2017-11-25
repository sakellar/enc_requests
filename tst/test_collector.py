import unittest
import json
from main_module import RequestBuilder
from main_module import Collector
from main_module import requests
import mock
from mock import patch


class TestCollector(unittest.TestCase):

    def test_request_build(self):
        collector = Collector(["--since", "2011-11-15 10:00:00", "--until", "2016-06-05 10:00:00"])
        new_request = RequestBuilder(collector.since, collector.until)
        expected_uri1 = "https://api.stackexchange.com/2.2/answers?pagesize=20&fromdate="+str(collector.since) +"&todate="+str(collector.until)+"&order=desc&sort=activity&site=stackoverflow&filter=!40nvjHTUxmmwZk05W"
        self.assertEquals(expected_uri1, new_request.get_answer_uri())
        question_id = "44118002"
        expected_uri2 = "https://api.stackexchange.com/2.2/questions/44118002?order=desc&sort=activity&site=stackoverflow&filter=!--KJ7Yfz(k3H"
        self.assertEquals(expected_uri2, new_request.get_question_uri(44118002))

    @patch.object(requests, 'get')
    def test_parse_get_response_from_stackexchange(self, requests_get):
        collector = Collector(["--since", "2011-11-15 10:00:00", "--until", "2016-06-05 10:00:00"])
        f = open("test_question.json")
        class mock_requests:
            status_code = 200
            text = None
        mock_object = mock_requests
        mock_object.text  = f.read()
        f.close()
        requests_get.return_value = mock_object
        expected_answer = 6
        self.assertEquals(collector.parse_answer_count(45535808), expected_answer)
        f = open("test.json")
        mock_object1 = mock_requests
        mock_object1.text  = f.read()
        f.close()
        uri = "whatever"
        requests_get.return_value = mock_object1
        collector.get_stackexchange_data()
        expected_answer = mock_object1.text
        self.assertEquals(collector.answer, expected_answer)

    @patch('main_module.Collector.get_stackexchange_data')
    @patch.object(Collector, 'parse_answer_count', return_value=3)
    def test_collect_statistics(self, parse_answer_count, get_stackexchange_data):
        uri = "whatever"
        collector = Collector(["--since", "2016-06-04 10:00:00", "--until", "2016-06-05 10:00:00"])
        collector.get_stackexchange_data(uri)
        get_stackexchange_data.assert_called_once_with(uri)

        # fill asnwers with json file
        f = open("test.json")
        collector.answer = f.read()
        f.close()
        collector.collect_statistics()
        self.assertEqual(collector.results['total_accepted_answers'], 1)
        self.assertEqual(collector.results['accepted_answers_average_score'], 6.0)
        self.assertEqual(collector.results['average_answers_per_question'], 3.0)
        self.assertEqual(collector.results['top_ten_answers_comment_count'], {45535808: 0, 46051675: 0, 45017555: 4})
        collector.produce_report()

    @patch('main_module.Collector.get_stackexchange_data')
    @patch.object(Collector, 'parse_answer_count', return_value=3)
    def test_collect_statistics_html(self, parse_answer_count, get_stackexchange_data):
        uri = "whatever"
        collector = Collector(["--since", "2016-06-04 10:00:00", "--until", "2016-06-05 10:00:00", "--output-format", "html"])
        collector.get_stackexchange_data(uri)
        get_stackexchange_data.assert_called_once_with(uri)

        # fill asnwers with json file
        f = open("test.json")
        collector.answer = f.read()
        f.close()
        collector.collect_statistics()
        self.assertEqual(collector.results['total_accepted_answers'], 1)
        self.assertEqual(collector.results['accepted_answers_average_score'], 6.0)
        self.assertEqual(collector.results['average_answers_per_question'], 3.0)
        self.assertEqual(collector.results['top_ten_answers_comment_count'], {45535808: 0, 46051675: 0, 45017555: 4})
        collector.produce_report()

if __name__ == '__main__':
    unittest.main()
