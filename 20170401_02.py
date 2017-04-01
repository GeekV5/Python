#!/usr/bin/python
# -*- coding:UTF-8 -*-
import psutil

# psutil获取CPU信息
print '===============获取CPU信息=============='
print 'CPU的整个信息：'
print psutil.cpu_times()
print ''

print '获取CPU单项值:'
print psutil.cpu_times().user
print ''

print '获取CPU的逻辑个数：'
print psutil.cpu_count()
print ''

print '获取CPU的物理个数：'
print psutil.cpu_count(logical=False)
print ''

print '===============获取内存信息=============='
mem = psutil.virtual_memory() #获取内存的完整信息
print '获取内存总数：'
print mem.total
print ''

print '获取空闲的内存信息：'
print mem.free
print ''

print '获取SWAP分区信息：'
print psutil.swap_memory()
print ''

print '===============获取磁盘信息=============='

print '获取磁盘IO信息：'
print psutil.disk_io_counters()
print ''

print '获取磁盘的完整信息：'
print psutil.disk_partitions()
print ''

print '获取分区表的参数：'
print psutil.disk_usage('/')
print ''

print '获取单个分区IO个数：'
print psutil.disk_io_counters(perdisk=True)#perdisk=True 参数获取单个分区IO个数
print ''

print '===============获取网络信息=============='





