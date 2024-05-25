"""
Tests the expansion and parsing of tossups and bonuses from a word document.
"""
from src.typeParsers.docxParser import *
from docx import Document

TEST_FILE = "tests/data/testpacket.docx"

def test_get_next_text():
    doc = Document(TEST_FILE)

    answer = get_next_text(doc, 10)
    assert answer == "ANSWER: clays [accept clay minerals; prompt on sediment; prompt on dirt; prompt on soil before it is \nread]"

    bonus = get_next_text(doc, 118)
    assert bonus == "[10h] This successor to LIGO could enable the detection of ultra-compact binaries and intermediate mass \nblack hole binaries by operating at much lower frequencies. It consists of three spacecraft that \nform an equilateral triangle and is planned to launch in 2037."

def test_get_next_text_overflow():
    doc = Document(TEST_FILE)
    error = get_next_text(doc, 14432)
    assert error == None

def test_full_packet():
    tossups, bonuses = get_tossups_and_bonuses(TEST_FILE)
    assert len(tossups) == 19564
    assert len(bonuses) == 19589