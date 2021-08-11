# -*- coding: utf-8 -*-
# @Time     : 2021/6/9 15:57
# @Author   : 宁星星
# @Email    : shenzimin0@gmail.com
import json


def get_trigger(data_dir):
    train_data = open(data_dir, 'r', encoding='utf8')
    for line in train_data:
        line = line.strip()
        line = json.loads(line)
