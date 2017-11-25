from optparse import OptionParser
import datetime
import logging

class Parser:
    """Parser Class which initializes parser with provided options"""
    time_format = "%Y-%m-%d %H:%M:%S"

    def __init__(self, args):
        """Parser class __init__ """
        self.parser = self._initialize_parser()
        (self.options, self.args) = self.parser.parse_args(args)
        self.since = None
        self.until = None
        self.format = "tab"
        if not self._check_options():
            return
        if not self._parse_dates():
            return
        if not self._parse_format():
            return


    def _initialize_parser(self):
        """Initializes Parser"""
        parser = OptionParser("stats --since <date>  --until <date> [--output-format] <tab|json|html>")
        parser.add_option("--since", action="store_true", dest="since",
                      help="1.  start date of request")
        parser.add_option("--until", action="store_true", dest="until",
                      help="2.  end date of request")
        parser.add_option("--output-format", action="store_true", dest="format",
                      help="3.  format of output tab, json, html")
        return parser

    def _check_options(self):
        """
        Counts the number of options against 1
        """
        option_counter = 0

        if self.options.since and self.options.until:
            if self.options.format:
                if len(self.args) == 3:
                    return True
                else:
                    self.parser.error("You need to provide format argument")
                    return False
            else:
                return True
        else:
            self.parser.error("You need to give --since and --until dates")
            return False

    def _parse_dates(self):
        """Checks for since and until dates mandatory arguments and converts them to unix timestamp"""
        try:
            self.since = self.args[0]
            self.until = self.args[1]
            self.since = int((datetime.datetime.strptime(self.since, self.time_format) - datetime.datetime(1970,1,1)).total_seconds())
            self.until = int((datetime.datetime.strptime(self.until, self.time_format) - datetime.datetime(1970,1,1)).total_seconds())
            return True
        except ValueError as e:
            self.parser.error("You need to give a valid date format %Y-%m-%d %H:%M:%S for since and until dates")
            return False
        except Exception as gene:
            self.parser.error("You need to give valid dates for since and until options")
            return False

    def _parse_format(self):
        """Checks for format optional argument"""
        try:
            if self.options.format:
                 self.format = self.args[2]
                 if (self.format == "json") or (self.format == "tab") or (self.format == "html"):
                     return True
                 else:
                     raise ValueError
            return True
        except ValueError as e:
            self.parser.error("You need to give a valid output format tab, json , html")
            return False
        except Exception as gene:
            self.parser.error("--option needs to be followed by a valid format")
            return False
