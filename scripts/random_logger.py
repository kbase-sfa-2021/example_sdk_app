#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.INFO)

from random import random


def main():
    index = 0
    value = random()
    while value > 1e-2:
        if (index % 10) == 0:
            logging.error(f"Still running after {index} trials")
        value = random()
        index += 1
    print(f"Computed value: {value} after {index} trials")


if __name__ == "__main__":
    main()
