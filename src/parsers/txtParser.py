"""
Defines functions for parsing a .txt file to extract tossups and bonuses.

Author: Will Hoover
"""

def get_tossups_and_bonuses(filename: str) -> tuple:
    """
    Returns a tuple of (tossup list, bonus list) for each individual tossup and bonus
    set in the parsed packet.
    """ 
    tossups = ""
    bonuses = ""
    with open(filename, 'r') as packet:
        # Get Tossups
        tossups_started = False
        while not tossups_started:
            line = packet.readline().strip()
            while line == "":
                line = packet.readline().strip()
            if line[0] == "1":
                tossups += line + '\n'
                tossups_started = True
        line = packet.readline().strip()
        while line.lower()[0:7] != "bonuses":
            tossups += line + '\n'
            line = packet.readline().strip()
            while line == "":
                line = packet.readline().strip()
        
        # Get Bonuses
        on_last_bonus = False
        line = packet.readline().strip()
        while not on_last_bonus or line != '':
            while not on_last_bonus and line == "":
                line = packet.readline().strip()
                if line[:2] == "20":
                    on_last_bonus = True
            bonuses += line + '\n'
            line = packet.readline().strip()

    return tossups, bonuses

def insert_newlines(filename: str, file_out=None):
    """
    Inserts newlines into a .txt file that was copy/pasted over so tossups don't exist on
    a single line.
    """
    if filename.split(".")[-1] != "txt":
        raise TypeError("File type cannot have newlines inserted")
    if file_out == None:
        file_out = filename
    new_file_text = ""
    with open(filename, 'r') as packet:
        line = packet.readline()
        while line:
            if len(line) < 100:
                new_file_text += line
            else:
                words = line.strip().split(" ")
                new_line = ""
                while len(words) > 0:
                    new_line += words.pop(0)
                    if len(new_line) > 100:
                        new_file_text += new_line + '\n'
                        new_line = ""
                    else:
                        new_line += " "
                if len(new_line) > 0:
                    new_file_text += new_line + '\n'
            line = packet.readline()
    with open(file_out, 'w') as revised:
        revised.write(new_file_text)