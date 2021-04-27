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

@app.route('/aging', methods=['GET'] or ['POST'])
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
    # 远程对服务器进行top指令查询
    stdin, stdout, stderr = ssh.exec_command("free -m | sed -n '2p' | awk '{print $(NF)}'",get_pty=True)
    AVAILABLE_MEMORY = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep '%Cpu' -A 0 | awk '{print $8}'",get_pty=True)
    CPU = float(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command('netstat -an | grep tcp | wc -l',get_pty=True)
    TCP_CONNECT = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("df -m / | sed -n '2p' | awk '{print $4}'",get_pty=True)
    SPACE_SIZE_GEN = str(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("df -m /tdfs | sed -n '2p' | awk '{print $4}'",get_pty=True)
    SPACE_SIZE_TDFS = str(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep 'Tasks' -A 0 | awk '{print $(NF-1)}'",get_pty=True)
    ZOMBIE = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep java_tomcat$ | awk '{print $(NF-7)}'",get_pty=True)
    TOMCAT_VIRT = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep java_tomcat$ | awk '{print $(NF-6)}'",get_pty=True)
    TOMCAT_RES = str(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep java_tomcat$ | awk '{print $(NF-3)}'",get_pty=True)
    TOMCAT_CPU = float(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep x1$ | awk '{print $(NF-7)}'",get_pty=True)
    X1_VIRT = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep x1$ | awk '{print $(NF-6)}'",get_pty=True)
    X1_RES = str(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep x1$ | awk '{print $(NF-3)}'",get_pty=True)
    X1_CPU = float(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep mysqld$ | awk '{print $(NF-7)}'",get_pty=True)   
    MYSQL_VIRT = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep mysqld$ | awk '{print $(NF-6)}'",get_pty=True)
    MYSQL_RES = str(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep mysqld$ | awk '{print $(NF-3)}'",get_pty=True)
    MYSQL_CPU = float(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep java_cassa | awk '{print $(NF-7)}'",get_pty=True)
    CASSANDRA_VIRT = int(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep java_cassa | awk '{print $(NF-6)}'",get_pty=True)
    CASSANDRA_RES = str(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | grep java_cassa | awk '{print $(NF-3)}'",get_pty=True)
    CASSANDRA_CPU = float(stdout.read().decode('utf-8'))
    ssh.close() # 关闭连接

    data = {
    'AVAILABLE_MEMORY' : AVAILABLE_MEMORY,
    'CPU' : CPU,
    'TCP_CONNECT' : TCP_CONNECT,
    'SPACE_SIZE_GEN' : SPACE_SIZE_GEN,
    'SPACE_SIZE_TDFS' : SPACE_SIZE_TDFS,
    'ZOMBIE' : ZOMBIE,
    'TOMCAT_VIRT' : TOMCAT_VIRT,
    'TOMCAT_RES' : TOMCAT_RES,
    'TOMCAT_CPU' : TOMCAT_CPU,
    'X1_VIRT' : X1_VIRT,
    'X1_RES' : X1_RES,
    'X1_CPU' : X1_CPU,
    'MYSQL_VIRT' : MYSQL_VIRT,
    'MYSQL_RES' : MYSQL_RES,
    'MYSQL_CPU' : MYSQL_CPU,
    'CASSANDRA_VIRT' : CASSANDRA_VIRT,
    'CASSANDRA_RES' : CASSANDRA_RES,
    'CASSANDRA_CPU' : CASSANDRA_CPU
    }
    # 此为API接口的标准格式
    return_dict = {
    'code' : 200,
    'message' : '成功',
    'data' : data
    }
    return json.dumps(return_dict, ensure_ascii=True) # JSON格式对齐

    # data = [AVAILABLE_MEMORY, CPU, TCP_CONNECT, SPACE_SIZE_GEN, SPACE_SIZE_TDFS, ZOMBIE, TOMCAT_VIRT, TOMCAT_RES, TOMCAT_CPU, X1_VIRT, X1_RES, X1_CPU, MYSQL_VIRT, MYSQL_RES, MYSQL_CPU, CASSANDRA_VIRT, CASSANDRA_RES, CASSANDRA_CPU]
    logger.debug(return_dict)

    # return render_template('aging.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True) # threaded=True为开启多线程
