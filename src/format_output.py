import json
import json2html
from json2html import *
import unittest

class FormatOutput:
    """
    Class with methods which transform results
    to chosen format
    """

    def __init__(self, results, output_format="tab"):
        self.format = output_format
        self.results = results
    
    def produce_report(self):
        """Produces report"""
        if self.format == "tab":
            return self.produce_tabular()
        elif self.format == "json":
            return self.produce_json()
        elif self.format == "html":
            return self.produce_html()

    def produce_and_print_report(self):
        """Prints output produced by produce_report method"""
        report = self.produce_report()
        print report

    def produce_tabular(self):
        """Returns output in tabular format"""
        output = ""
        output += "total_accepted_answers :\t\t"  + str(self.results['total_accepted_answers']) + "\n"
        output += "accepted_answers_average_score :\t" + str(self.results['accepted_answers_average_score']) + "\n"
        output += "average_answers_per_question :\t\t"  + str(self.results['average_answers_per_question']) + "\n"
        output += "top_ten_answers_comment_count:\n"
        for key, value in self.results['top_ten_answers_comment_count'].iteritems():
            output +=  "\t" + str(key) + " :\t" + str(value) + "\n"
        return output

    def produce_json(self):
        """Returns output in json format"""
        return json.dumps(self.results)

    def produce_html(self):
        """Returns output in html format"""
        return json2html.convert(self.results)
