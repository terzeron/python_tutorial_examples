#!/usr/bin/env python

from util import Util


if __name__ == "__main__":
    conf = Util.read_config("conf.json")
    print(conf)