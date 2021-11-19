#!/usr/bin/env python

import logging

from random import random

def main():
    index = 0
    value = random()
    while value > 1e-2:
        if(index % 10) == 0:
            logging.warning(f"Still running after {index} trials")
        value = random()
        index += 1
    logging.error(f"Computed value: {value} after {index} trials")


if __name__ == "__main__":
    main()
