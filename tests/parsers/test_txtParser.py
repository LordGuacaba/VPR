"""
Tests the expansion and parsing of raw text from .txt files into tossups and bonuses sections.
"""
from src.parsers.txtParser import *

TEST_FILE = "tests/data/testpacket.txt"
NEWLINES_NEEDED = "tests/data/newlines_needed.txt"
INSERTED = "tests/data/newlines_inserted.txt"

def test_insert_newlines_txt():
    insert_newlines(NEWLINES_NEEDED, INSERTED)
    with open(INSERTED, "r") as file:
        file.readline()
        line = file.readline().strip()
        nextline = file.readline().strip()
        assert line == "1. To protect Bindusara from poison, Chanakya performed this action and subsequently placed Bindusara"
        assert nextline == "inside the stomachs of goats for seven days. This action was performed on a dying Clothru at Lough (“lock”)"
    with open(INSERTED, "w") as file:
        file.write("")

def test_insert_newlines_docx():
    try:
        insert_newlines("src/tests/data/testpacket.docx")
        assert False
    except TypeError:
        assert True

def test_full_packet():
    tossups, bonuses = get_tossups_and_bonuses(TEST_FILE)
    assert len(tossups) == 19125
    assert len(bonuses) == 19307