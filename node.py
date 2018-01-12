import socket
import sys
import tcode

from helpers import exit_with_stderr


IP = ''


class Node(object):
    def __init__(self, port, s):
        self.port = port
        self.s = s
        self.counter = 0
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def deliver(self, message, destination):
        self.s.sendto(message, (IP, destination))

    def act(self, message, addr):
        try:
            payload = tcode.decode_list(['str'] * 5, message)
        except IndexError:
            payload = tcode.decode_list(['str'] * 7, message)

        if payload[0] == 'req' and payload[1] == str(self.port):
            key = payload[4]

            if len(payload) == 5:
                value = self.data.get(key)
                if value:
                    print 'GET ' + key + ':' + self.get(key)
                else:
                    sys.stderr.write("key not found\n")

            elif len(payload) == 7:
                value = payload[6]
                self.set(key, value)
                print 'SET ' + key + ':' + self.get(key)

        elif payload[0] == 'req' and payload[1] != str(self.port):
            message = tcode.encode_list(['str'] * len(payload), payload)
            self.deliver(message, int(payload[1]))

    def start(self):
        while True:
            try:
                self.s.settimeout(3)
                message, addr = self.s.recvfrom(1024)
                print message
                self.act(message, addr)
            except socket.timeout:
                print '.'


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


if __name__ == '__main__':
    port = parse_arguments()
    s = bind_socket(port)

    node = Node(port, s)
    node.start()
