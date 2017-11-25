# encode_requests

Retrieve the StackOverflow answer data for a given date/time range from the StackExchange API
(https://api.stackexchange.com/docs/answers).
Retrieve the comment data for a given set of answers (https://api.stackexchange.com/docs/comments­on­answers).
For a given date/time range calculate:
the total number of accepted answers.
the average score for all the accepted answers.
the average answer count per question.
the comment count for each of the 10 answers with the highest score.
Collect and return the calculated statistics in tabular, HTML or JSON format.

## REQUIREMENTS
Install python mock
```
$ sudo pip install mock
```

## INSTALL
Alternatevely if you have donwloaded source code:
```
python setup.py install
```

## Documentation
```
bash run_tests.sh
```
