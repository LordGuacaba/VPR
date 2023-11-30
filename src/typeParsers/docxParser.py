"""
Defines functions for parsing a .docx file to extract tossups and bonuses.

Author: Will Hoover
"""
from typeParsers.formatter import format_tossups, format_bonuses
from docx import Document

PARAGRAPH_INDEX = 0

def get_next_text(document):
    """
    Returns the text of then next paragraph in the document based on the global
    current paragraph index.
    """
    global PARAGRAPH_INDEX
    try:
        text = document.paragraphs[PARAGRAPH_INDEX].text.strip()
        if len(text) > 100:
            next_hundred = 1
            words = text.split(" ")
            text = ""
            for word in words:
                text += word + " "
                if len(text) > next_hundred * 100:
                    text += "\n"
                    next_hundred += 1
        PARAGRAPH_INDEX += 1
        return text
    except(IndexError):
        return None

def get_tossups_and_bonuses(filename: str) -> tuple:
    """
    Returns a tuple of (tossup list, bonus list) for each individual tossup and bonus
    set in the parsed packet.
    """ 
    tossups = ""
    bonuses = ""
    doc = Document(filename)
    tossups_started = False
    while not tossups_started:
        text = get_next_text(doc)
        while text == "":
            text = get_next_text(doc)
        if text[0] == "1":
            tossups += text + '\n'
            tossups_started = True
    text = get_next_text(doc)
    while text.lower()[0:7] != "bonuses":
        tossups += text + "\n"
        text = get_next_text(doc)
        while text == "":
            text = get_next_text(doc)

    text = get_next_text(doc)
    while text != None:
        while text == "":
            text = get_next_text(doc)
        bonuses += text + "\n"
        text = get_next_text(doc)
    
    return format_tossups(tossups), format_bonuses(bonuses)