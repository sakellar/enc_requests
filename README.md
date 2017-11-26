# encode_requests

For a given date/time range calculates:

1. the total number of accepted answers.
2. the average score for all the accepted answers.
3. the average answer count per question.
4. the comment count for each of the 10 answers with the highest score.
5. Collects and returns the calculated statistics in tabular, HTML or JSON format.

## REQUIREMENTS
Install python mock.
```
$ sudo pip install mock
```

```
$ sudo pip install requests
```

## INSTALL
Alternatevely if you have donwloaded source code:
```
python setup.py install
```
## HOW TO RUN IT
Inside src code Run:

```
alias stats=python main_module.py
```

```
$ stats --help
Usage: stats --since <date>  --until <date> [--output-format] <tab|json|html>

Options:
  -h, --help       show this help message and exit
  --since          1.  start date of request
  --until          2.  end date of request
  --output-format  3.  format of output tab, json, html
```
You have to provide since date and until date, output-format is optional and defaults to tab:
```
stats --since '2011-11-15 10:00:00' --until '2016-06-05 10:00:00' -output-format html
```

Assumptions: 
Only 20 pages are retrieved per request. It is easy to change the code for 100 pages which is the maximum page size limit.

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
