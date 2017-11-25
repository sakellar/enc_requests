export PYTHONPATH=.
PYTHONPATH=$PYTHONPATH:../src
python -m unittest test_parser 
python -m unittest test_format_output 
python -m unittest test_collector 
