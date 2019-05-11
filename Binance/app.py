import backtest as backtest
import sys, getopt, json, time, datetime, argparse

def main(argv):
    # backtest.golden_cross(argv.pair)
    # run_backtest_one(argv.pair)
    run_backtest_two(argv.pair)

def run_backtest_one(pair):
    backtest.test_one(pair)

def run_backtest_two(pair):
    backtest.test_two(pair)

def parse_arguments():
    # Holds all the information necessary to aprse the command line into Python data types.
    parser = argparse.ArgumentParser()
    
    # arguments:
    #   -h                  Show this help message and exit.
    #   -p, --pair          The currency to backtest on.
    parser.add_argument('-p','--pair', help='The pair to backtest on in the format XXXYYY',type=str)

    
    args = parser.parse_args() 

    if args.pair is None:
        print('Please enter a pair in the format -p XXXYYY in the command line when calling this script.'
                + '\nFor example, if you would like to backtest on the BTC data, you would enter the command:'
                + '\n\npython backtest.py -p BTCUSDT')
        sys.exit()
    return args

if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)