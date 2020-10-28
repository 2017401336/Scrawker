#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2020/10/22 11:39
# @Author　 : RoadGod
# @Project  : crawker
# @File　　 : 1.认识json在python中的运用.py
# @Software : PyCharm
import json

'''
def dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
    allow_nan=True, cls=None, indent=None, separators=None,
    default=None, sort_keys=False, **kw)
    
def load(fp, *, cls=None, object_hook=None, parse_float=None,
    parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    
def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
    allow_nan=True, cls=None, indent=None, separators=None,
    default=None, sort_keys=False, **kw)
    
def loads(s, *, cls=None, object_hook=None, parse_float=None,
    parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    
_default_encoder = JSONEncoder(
    skipkeys=False,         # 如果为True的话，则只能是字典对象，否则会TypeError错误, 默认False
    ensure_ascii=True,      # 确定是否为ASCII编码
    check_circular=True,    # 循环类型检查，如果为True的话
    allow_nan=True,         # 确定是否为允许的值
    indent=None,            # 会以美观的方式来打印，呈现，实现缩进
    separators=None,        # 对象分隔符，默认为, 
    default=None,           # 编码方式,默认为utf-8     
    sort_keys=False,        # 如果是字典对象，选择True的话，会按照键的ASCII码来排序    
)
'''
if __name__ == "__main__":
    # dumps()
    data = {'name': 'IU', 'age': 18}
    json_data = json.dumps(data)
    # {"name": "IU", "age": 18}
    print(json_data)
    # json_data
    print(type(json_data))
    _data = json.loads(json_data)
    # <class 'dict'>
    print(type(_data))
    # IU 18
    print(_data['name'], _data['age'])
    with open('./IU.txt', 'w') as fp:
        json.dump(_data, fp)
    print('json.dump写入数据成功')
    with open('./IU.txt', 'r') as fp:
        data_ = json.load(fp)
    print('json.load读取数据：' + str(data_))

