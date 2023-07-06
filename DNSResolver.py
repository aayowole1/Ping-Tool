import socket

def resolve(hostname):
    return socket.gethostbyname(hostname)