"""
    - ccirc - Coding Challenge IRC Client
    - Writing my own IRC Client (https://codingchallenges.fyi/challenges/challenge-irc/)
    
    main.py
"""

import socket
import time

# IRC Config Settings
SERVER = "irc.freenode.net"
PORT = 6667
NICK = "ccclient_nik"


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

        response = irc.recv(2040).decode("UTF-8")

        print(response)

        # Deal with PING/PONG cycle as per protocol
        if response.find("PING") != -1:
            irc.send(bytes("PONG " + response.split()[-1] + "\r\n", "UTF-8"))


if __name__ == "__main__":
    main()
