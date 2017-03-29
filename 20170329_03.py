#!/usr/bin/python
# -*- coding:UTF-8 -*-
import json
# 将数组编码为JSON格式数据

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json = json.dumps(data)
print json