#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import json

import paramiko
from flask import Flask, jsonify, render_template, request
from loguru import logger

# json转换中文不使用unicode
JSON_AS_ASCII = False

# 实例化Flask
app = Flask(__name__)
app.config.from_object(__name__)

# 配置路由
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aging', methods=['GET'])
def get_aging():
    get_data = request.args.to_dict() # 获取传入的参数
    logger.debug(get_data)
    IP_ADDRESS = get_data.get('IP_ADDRESS')
    PORT = get_data.get('PORT')
    USER = get_data.get('USER')
    PASSWORD = get_data.get('PASSWORD')

    # 通过SSH连接读取服务器信息
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP_ADDRESS,PORT,USER,PASSWORD)
    stdin, stdout, stderr = ssh.exec_command("free -m | sed -n '2p' | awk '{print$(NF)}'")
    AVAILABLE_MEMORY = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("df -m / | sed -n '2p' | awk '{print$4}'")
    SPACE_SIZE = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command('netstat -an | grep tcp | wc -l')
    TCP_CONNECT = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep '%Cpu' -A 0 | awk '{print$8}'")
    CPU = float(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep 'Tasks' -A 0 | awk '{print$(NF-1)}'")
    ZOMBIE = int(stdout.read().decode('utf-8'))
    ssh.close() # 关闭连接
    '''
    return_dict = {
    'AVAILABLE_MEMORY' : AVAILABLE_MEMORY,
    'SPACE_SIZE' : SPACE_SIZE,
    'TCP_CONNECT' : TCP_CONNECT,
    'CPU' : CPU,
    'ZOMBIE' : ZOMBIE,
    } # 返回参数
    return json.dumps(return_dict, ensure_ascii=False) # JSON格式对齐
    '''
    return_dict = [AVAILABLE_MEMORY, SPACE_SIZE, TCP_CONNECT, CPU, ZOMBIE]
    logger.debug(return_dict)

    return render_template('aging.html', return_dict=return_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True) # threaded=True为开启多线程
