"""
Defines functions for parsing a .txt file to extract tossups and bonuses.

Author: Will Hoover
"""


def get_tossups_and_bonuses(filename: str) -> tuple:
    tossups = ""
    bonuses = ""
    with open(filename, 'r') as packet:
        # Get Tossups
        tossups_started = False
        while not tossups_started:
            line = packet.readline().strip()
            if line[0] == '1':
                tossups += line + '\n'
                tossups_started = True
        line = packet.readline().strip()
        while line.lower()[0:6] != "bonuses":
            tossups += line + '\n'
            line = packet.readline().strip()
        
        
        # Get Bonuses

        
    

def format_tossups():
    pass

def format_bonuses():
    pass