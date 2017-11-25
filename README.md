# encode_requests

Retrieve the StackOverflow answer data for a given date/time range from the StackExchange API (https://api.stackexchange.com/docs/answers).
Retrieve the comment data for a given set of answers (https://api.stackexchange.com/docs/comments­on­answers).
For a given date/time range calculates:
the total number of accepted answers.
the average score for all the accepted answers.
the average answer count per question.
the comment count for each of the 10 answers with the highest score.
Collects and returns the calculated statistics in tabular, HTML or JSON format.

## REQUIREMENTS
Install python mock.
```
$ sudo pip install mock
```

## INSTALL
Alternatevely if you have donwloaded source code:
```
python setup.py install
```
## HOW TO RUN IT
Inside src code Run:
```
$ python main_module.py --help
Usage: stats --since <date>  --until <date> [--output-format] <tab|json|html>

Options:
  -h, --help       show this help message and exit
  --since          1.  start date of request
  --until          2.  end date of request
  --output-format  3.  format of output tab, json, html
```
You have to provide since date and until date, output-format is optional and defaults to tab:
```
python main_module.py --since '2011-11-15 10:00:00' --until '2016-06-05 10:00:00' -output-format html
```

Assumptions: 
Only 20 pages are retrieved. It is easy to change the code for 100 pages which is the maximum limit for stackoverflow.

## TESTING
```
bash run_tests.sh
```
Alternatively you can run explicitily tests:
```
python -m unittest test_parser
```
```
python -m unittest test_format_output
```
```
python -m unittest test_collector
```
