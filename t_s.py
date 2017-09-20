#! /usr/bin/env python3  
#-*- coding=utf-8 -*-  
  
# ============================  
# Describe :    给平台提供的日志   
# Modify Date:     2017/08/10  
# ============================ 
"""
@author: shikinami
@software: PyCharm Community Edition
@file: t_s.py
@time: 17-9-18 下午4:04
"""
import socket
class Main(object):
    host = '127.0.0.1'
    port = 8080
    def __init__(self):
        self.ip_port = (self.host,self.port)
        self.t_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.t_s.bind(self.ip_port)
        self.t_s.listen(5)

    def create_line(self):
        while 1:
            self.conn,self.address = self.t_s.accept()
            print(self.conn)
            print(type(self.conn))
            self.conn.send('hello.'.encode())
            self.conn.close()


if __name__ == '__main__':
    '''
    This is test template
    '''
    obj = Main()
    obj.create_line()