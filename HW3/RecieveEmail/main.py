#!/usr/bin/env python3

import socket
import base64


def init_connection(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    return s


def send_email(subject, body, src_email, dst_email, username, password, sock):
    sock.send('HELO mail.email.com\r\n'.encode('utf-8'))
    sock.send('AUTH LOGIN\r\n'.encode('utf-8'))
    sock.send(base64.b64encode(username.encode('utf-8')) + '\r\n'.encode('utf-8'))
    sock.send(base64.b64encode(password.encode('utf-8')) + '\r\n'.encode('utf-8'))
    sock.send(('MAIL FROM:' + src_email + '\r\n').encode('utf-8'))
    sock.send(('RCPT TO:' + dst_email + '\r\n').encode('utf-8'))
    sock.send(('DATA\r\n').encode('utf-8'))
    sock.send(('Subject: ' + subject + '\r\n\r\n').encode('utf-8'))
    sock.send((body + '\r\n').encode('utf-8'))
    sock.send('.\r\n'.encode('utf-8'))
    sock.send('QUIT\r\n'.encode('utf-8'))
    sock.close()

if __name__ == '__main__':
    src_email = input('Enter your email address:')
    dst_email = input('Enter your destination address:')
    subject = input('Enter your subject:')
    server = input('Enter you server address:')
    username = input('Enter your username:')
    password = input('Enter your password:')
    port = input('Enter you server port:')
    body = input('Enter your email body:')

    sock = init_connection(server, int(port))
    send_email(subject, body, src_email, dst_email, username, password, sock)
