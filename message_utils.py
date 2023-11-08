"""
    - ccirc - Coding Challenge IRC Client
    - Writing my own IRC Client (https://codingchallenges.fyi/challenges/challenge-irc/)
    
    - Message util functions
    
    message_utils.py
"""

import re


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
