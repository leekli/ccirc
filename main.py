"""
    - ccirc - Coding Challenge IRC Client
    - Writing my own IRC Client (https://codingchallenges.fyi/challenges/challenge-irc/)
    
    main.py
"""

""" TO DO:
    - Build protocol handler and extract out
    - Build proper message parser once protocol handled
    - Extract out config settings
"""

import socket
import time
import re

# IRC Config Settings
SERVER = "irc.freenode.net"
PORT = 6667
NICK = "ccircx"


def format_socket_msg(msg):
    notice_pattern = r":\*\.\w+\.\w+ NOTICE (\w+|\*) :\*\*\* "
    server_msg_pattern = r":.*? \d{3} \w+ :"
    ping_pattern = r"PING :\*\.[-\w]+(?:\.\w+)+"
    notice_match = re.search(notice_pattern, msg)
    server_msg_match = re.search(server_msg_pattern, msg)
    ping_match = re.search(ping_pattern, msg)
    formatted_response = ""

    if notice_match:
        formatted_response = re.sub(notice_pattern, "", msg)

    if server_msg_match:
        formatted_response = re.sub(server_msg_pattern, "", msg)

    if ping_match:
        formatted_response = re.sub(ping_pattern, "PING Received.", msg)

    return formatted_response


def main():
    # New socket instance
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to IRC server with config and initial 2 IRC protocol messages
    print(f"Connecting to {SERVER} on port {PORT}...")

    irc.connect((SERVER, PORT))
    irc.send(bytes("USER guest 0 * :Coding Challenges Client\n", "UTF-8"))
    irc.send(bytes(f"NICK {NICK}\n", "UTF-8"))

    # Loop for constantly checking messages
    while True:
        time.sleep(1)

        response = format_socket_msg(irc.recv(1024).decode("UTF-8").strip("\r\n"))

        # Deal with PING/PONG cycle as per protocol
        if response.find("PING") != -1:
            irc.send(bytes("PONG " + response.split()[-1] + "\r\n", "UTF-8"))


if __name__ == "__main__":
    main()
