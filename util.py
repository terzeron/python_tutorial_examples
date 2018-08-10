#!/usr/bin/env python

import json


class Util:
    @staticmethod
    def read_config(config_file):
        with open(config_file, "r") as infile:
            result = []
            for line in infile:
                result.append(line)
            json_data = "".join(result)
            return json.loads(json_data)

    @staticmethod
    def write_config(config_file):
        # blah blah
        # blah blah
        None
