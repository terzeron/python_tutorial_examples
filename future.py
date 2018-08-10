#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor, as_completed


def func(data):
    return data * 10;


data_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(func, data): data for data in data_list}
    for f in as_completed(futures):
        data = futures[f]
        try:
            result = f.result()
            print(result)
        except Exception as e:
            raise e


