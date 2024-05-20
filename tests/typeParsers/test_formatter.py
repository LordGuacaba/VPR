"""
Tests the functions for formatting raw text into tossup and bonus objects.
"""
from src.typeParsers.formatter import *
from src.typeParsers.txtParser import get_tossups_and_bonuses

def test_is_start_of_question_true():
    one_digit = "3. This object came into Smeagol's possession after centuries of lurking in"
    two_digit = "14. For 10 points each, name some delicious pasta dishes that can be made by"

    assert is_start_of_question(one_digit)
    assert is_start_of_question(two_digit)

def test_is_start_of_question_random_number():
    line = "10 rocks are devoured by Michael in, for 10 points, what Goethe work in which"
    three_digit = "101 Nights, this character is depicted sitting on a television during the Chicago"

    assert not is_start_of_question(line)
    assert not is_start_of_question(three_digit)

def test_is_start_of_question_false():
    line = "ethnicity married a princess whom Anna Komnene described in battle as like “a second Athena,” named"
    assert not is_start_of_question(line)

def test_remove_bad_stuff_numbering():
    one_digit = "3. This object came into Smeagol's possession after centuries of lurking in"
    two_digit = "14. For 10 points each, name some delicious pasta dishes that can be made by"

    assert remove_bad_stuff(one_digit) == "This object came into Smeagol's possession after centuries of lurking in "
    assert remove_bad_stuff(two_digit) == "For 10 points each, name some delicious pasta dishes that can be made by "

def test_remove_bad_stuff_pronunciation():
    full_line = "Chiaretta (“k’yah-RAY-tuh”), the major collection by Triestini poet Umberto Saba. A poem in this collection"
    guide_start = "and analysis of these texts is “Introduction to the Science of” these texts. Ignác (“IG-"
    guide_end = "uh-lee-OO-muh”), whose grandson Muwatalli II signed a peace treaty with Ramses the Great after the"

    assert remove_bad_stuff(full_line) == "Chiaretta, the major collection by Triestini poet Umberto Saba. A poem in this collection "
    assert remove_bad_stuff(guide_start) == "and analysis of these texts is “Introduction to the Science of” these texts. Ignác  "
    assert remove_bad_stuff(guide_end) == ", whose grandson Muwatalli II signed a peace treaty with Ramses the Great after the "

def test_remove_bad_stuff_author():
    line = "<Christensen, Other History (Ancient)>"
    assert remove_bad_stuff(line) == ""

def test_full_packet_text():
    tossups, bonuses = get_tossups_and_bonuses("tests/data/testpacket.txt")
    tossup_list = format_tossups(tossups)
    bonus_list = format_bonuses(bonuses)

    assert len(tossup_list) == 20
    assert len(bonus_list) == 20

    assert tossup_list[5]["non-power"] == " “hope your road is a long one” in spite of “Laistrygonians, Cyclops, [and] angry Poseidon.” In another poem by this author, the speaker asks “Why are the senators sitting there without legislating?” before realizing that the title group was “a kind of solution.” For 10 points, name this Greek poet of “Ithaka” and “Waiting for the Barbarians.” "
    assert tossup_list[13]["answer"] == "ANSWER: San Francisco, California [accept San Fran] (the other film is Francis Ford Coppola’s The Conversation.) "

    assert bonus_list[5]["answer-2"] == "ANSWER: New Zealand [or Aotearoa] "
    assert bonus_list[15]["lead-in"] == "Elliptical orbits have a nonzero value for this quantity. For 10 points each: "
