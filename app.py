#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

from flask import Flask, jsonify, request

# 配置参数,开启debug模式,json转换中文不使用unicode
DEBUG = True
JSON_AS_ASCII = False

# 实例化Flask
app = Flask(__name__)
app.config.from_object(__name__)

# 配置路由
@app.route('/lh', methods=['GET'])
def get_aging():
    aging = request.args.get('IP_ADDRESS')
    # print(aging)
    if (aging == '127.0.0.1'):
        return dict(
            IP_ADDRESS='127.0.0.1',
            AVAILABLE_MEMORY='503',
            SPACE_SIZE='1823',
            TCP_CONNECT='130',
            CPU='6.1',
            ZOMBIE='0',
            JAVA_VIRT='3595.8m',
            JAVA_RES='925.2m',
            JAVA_CPU='2.5',
            X1_VIRT='3595.8m',
            X1_RES='925.2m',
            X1_CPU='2.5',
            MYSQL_VIRT='1530.1m',
            MYSQL_RES='9.6m',
            MYSQL_CPU='6.3',
        )
    else:
        return '404 Not Found!'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)
