import argparse
from itertools import cycle

from control.controller import LamportClocksController


def print_log():
    with open('result.log') as log:
        print(log.read())

def main(**kwargs):
    controller = LamportClocksController(**kwargs)
    controller.random_routine()
    # controller.test_routine()
    print_log()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Running Lamport Clocks')
    parser.add_argument("--num_clocks", help="This is the number of Lamport Clocks variable")
    parser.add_argument("--cycles", help="Number of routine cycles")
    args = parser.parse_args()
    main(num_clocks=int(args.num_clocks), cycles=int(args.cycles))
    # main(num_clocks=4, cycles=10)