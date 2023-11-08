"""
    - ccirc - Coding Challenge IRC Client
    - Writing my own IRC Client (https://codingchallenges.fyi/challenges/challenge-irc/)
    
    - Main Entry point
    
    main.py
"""

""" TO DO:
    - Build protocol handler and extract out
    - Build proper message parser once protocol handled
    - Extract out config settings
"""

import socket
import time
from config import SERVER, PORT, NICK
from message_utils import format_socket_msg


def main():
    # New socket instance
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to IRC server with config and initial 2 IRC protocol messages
    print(f"Connecting to {SERVER} on port {PORT}...")

    irc.connect((SERVER, PORT))
    irc.send(bytes("USER guest 0 * :Coding Challenges Client\n", "UTF-8"))
    irc.send(bytes(f"NICK {NICK}\n", "UTF-8"))

    # Message Loop
    while True:
        time.sleep(1)

        response = format_socket_msg(irc.recv(1024).decode("UTF-8").strip("\r\n"))

        print(response)

        # Deal with PING/PONG cycle as per protocol
        if response.find("PING") != -1:
            irc.send(bytes("PONG " + response.split()[-1] + "\r\n", "UTF-8"))


if __name__ == "__main__":
    main()
