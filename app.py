#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

from flask import Flask
from flask import jsonify

# 配置参数,开启debug模式,json转换中文不使用unicode
DEBUG = True
JSON_AS_ASCII = False

# 实例化Flask
app = Flask(__name__)
app.config.from_object(__name__)


# 配置路由
@app.route('/dd', methods=['GET'])
def ping():
    return jsonify('Flask!')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)