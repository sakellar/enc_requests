import unittest
from mock import Mock, patch, call
from parser import Parser, OptionParser

class TestParser(unittest.TestCase):

    def test_parse_options(self):
        parser = Parser(["--since", "2016-06-02 10:00:00", "--until", "2016-06-03 10:00:00"])
        expected_dict = {'since': True, 'until': True, 'format':None}
        self.assertEqual(parser.options, expected_dict) 

    def test_parse_options_format(self):
        parser = Parser(["--since", "2016-06-02 10:00:00", "--until", "2016-06-03 10:00:00", "--output-format", "json"])
        expected_dict = {'since': True, 'until': True, 'format':True}
        self.assertEqual(parser.options, expected_dict) 

    @patch("parser.OptionParser.error")
    def test_parse_wrong_options(self, mock_error):
           parser = Parser(["--nothing special"])
           parser2 = Parser(["--since", "whatever", "--until"])
           parser4 = Parser(["--since", "2016-06-02 10:00:00", "--until", "2016-06-03 10:00:00", "--output-format"])
           mock_error.assert_has_calls([call('no such option: --nothing special'),
                                         call('You need to give --since and --until dates'),
                                         call('You need to give valid dates for since and until options'),
                                         call('You need to provide format argument')])
if __name__ == '__main__':
    unittest.main()
