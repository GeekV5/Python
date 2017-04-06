#!/usr/bin/python
# -*- coding:UTF-8 -*-
import psutil

print psutil.net_io_counters(pernic=True)
print psutil.net_if_addrs()
print psutil.net_if_stats()
print psutil.users()
