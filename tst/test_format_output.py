import unittest
from mock import patch, mock_open, call, MagicMock, Mock
from format_output import FormatOutput


class TestFormatOuptut(unittest.TestCase):

     def test_init(self):
         """
         Tests init method of FormatOutput
         """
         results = dict()
         results['total_accepted_answers'] = 10
         results['accepted_answers_average_score'] = 5
         results['average_answers_per_question'] = 3
         results['top_ten_answers_comment_count'] = {"38149500": 1, "38152507": 7,}
         formatOutput  = FormatOutput(results, "json")
         self.assertEquals(formatOutput.format, "json")
         self.assertEquals(formatOutput.results, results)

     def test_tabular(self):
         results = dict()
         results['total_accepted_answers'] = 10
         results['accepted_answers_average_score'] = 5
         results['average_answers_per_question'] = 3
         results['top_ten_answers_comment_count'] = {"38149500": 1, "38152507": 7}
         formatOutput  = FormatOutput(results, "tab")
         output = formatOutput.produce_report()
         expected_output = "total_accepted_answers :\t\t10\naccepted_answers_average_score :\t5\naverage_answers_per_question :\t\t3\ntop_ten_answers_comment_count:\n\t38149500 :\t1\n\t38152507 :\t7\n"
         self.assertEquals(output, expected_output)

     def test_json(self):
         results = dict()
         results['total_accepted_answers'] = 10
         results['accepted_answers_average_score'] = 5
         results['average_answers_per_question'] = 3
         results['top_ten_answers_comment_count'] = {"38149500": 1, "38152507": 7}
         formatOutput  = FormatOutput(results, "json")
         output = formatOutput.produce_report()
         expected_output = '{"average_answers_per_question": 3, "accepted_answers_average_score": 5, "total_accepted_answers": 10, "top_ten_answers_comment_count": {"38149500": 1, "38152507": 7}}'
         self.assertEquals(output, expected_output)

     def test_html(self):
         results = dict()
         results['total_accepted_answers'] = 10
         results['accepted_answers_average_score'] = 5
         results['average_answers_per_question'] = 3
         results['top_ten_answers_comment_count'] = {"38149500": 1, "38152507": 7}
         formatOutput  = FormatOutput(results, "html")
         output = formatOutput.produce_report()
         expected_output = u'<table border="1"><tr><th>average_answers_per_question</th><td>3</td></tr><tr><th>accepted_answers_average_score</th><td>5</td></tr><tr><th>total_accepted_answers</th><td>10</td></tr><tr><th>top_ten_answers_comment_count</th><td><table border="1"><tr><th>38149500</th><td>1</td></tr><tr><th>38152507</th><td>7</td></tr></table></td></tr></table>'
         self.assertEquals(output, expected_output)

if __name__ == '__main__':
    unittest.main()
