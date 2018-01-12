import socket
import sys

from helpers import exit_with_stderr


IP = ''


def parse_arguments():
    try:
        port = int(sys.argv[1])
    except IndexError:
        exit_with_stderr("please specify a port number!")
    except ValueError:
        exit_with_stderr("please specify an integer!")

    return port


def bind_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP, port))
    return s


def listen_port(s):
    while True:
        try:
            s.settimeout(10)
            data, addr = s.recvfrom(1024)
            print data
            print addr
        except socket.timeout:
            print '.'


if __name__ == '__main__':
    port = parse_arguments()
    s = bind_socket(port)
    listen_port(s)