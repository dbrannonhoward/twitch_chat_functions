import CONSTANTS
import re
import socket

from time import sleep
from twitchAPI import twitch


def join_channel(twitch_socket, channel=CONSTANTS.CHAN):
    twitch_socket.send("PASS {}\r\n".format(CONSTANTS.PASS).encode('utf-8'))
    twitch_socket.send("NICK {}\r\n".format(CONSTANTS.NICK).encode('utf-8'))
    twitch_socket.send("JOIN {}\r\n".format(channel).encode('utf-8'))


def filter_message_only(response):
    pass


def get_twitch_instance(app_id=CONSTANTS.APP_ID, app_sec=CONSTANTS.APP_SECRET):
    # TODO placeholder
    pass  # TODO return twitch_object


def get_twitch_socket_instance(host=CONSTANTS.HOST, port=CONSTANTS.PORT):
    twitch_socket = socket.socket()
    twitch_socket.connect((host, port))
    return twitch_socket


def print_unfiltered_response(response):
    print(response)


def print_stream_metadata():
    # TODO placeholder
    pass  # TODO return dict/list of metadata


def main():
    twitch_socket = get_twitch_socket_instance()
    join_channel(twitch_socket)
    while True:
        response = twitch_socket.recv(1024).decode('utf-8')
        if response == 'PING :tmi.twitch.tv\r\n':
            twitch_socket.send('PONG :tmi.twitch.tv\r\n'.encode('utf-8'))
        else:
            print_unfiltered_response(response)
        sleep(0.5)
        # sleep(1 / CONSTANTS.RATE)


if __name__ == '__main__':
    main()
