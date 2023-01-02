import json,os
from re import L
filej = open('./ch3_zero.json','r',encoding='utf-8')
jsonp = json.loads(filej.read())
try:
    print(jsonp['is_hid'])
except KeyError as e:
    print('No is_hid key')
clear_type = 6
if clear_type in range(1,6):
    print('yes')