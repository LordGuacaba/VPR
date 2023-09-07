"""
Provides the functionality that directs the generation of the expanded-packet powerpoint.

@author Will Hoover
"""
from pptx import Presentation
from generator.pptx_utils import *

PACKET_TEMPLATE = "../templates/packet_template.pptx"
TOSSUP_SLIDE_HEADER = "Tossup #"
BONUS_SLIDE_HEADER = "Bonus #"

def get_tossup_fragments(tossup: str) -> list:
    no_add_list = [")", "?", "”", " "]
    period_split = tossup.split(".")
    fragments = list()
    for frag in period_split:
        frag += "."
        comma_split = frag.split(",")
        for i in range(len(comma_split)-1):
            fragments.append(comma_split[i] + ",")
        fragments.append(comma_split[-1])
    if fragments[-1][-2] in no_add_list:
        fragments[-1] = fragments[-1][:-1]
    return fragments

def add_tossup_slides(pres, header: str, tossup: dict):
    """
    Adds the expanded slides for a tossup to the presentation
    """
    current_slide = add_new_question(pres, header)
    power_frags = get_tossup_fragments(tossup["power"])
    non_power_frags = get_tossup_fragments(tossup["non-power"])
    for fragment in power_frags:
        current_slide = add_question_fragment(current_slide, pres, str(fragment))
    # The non-power and power fragments are split up partially for ease of logic, partly so the power clues can be bolded
    for fragment in non_power_frags:
        current_slide = add_question_fragment(current_slide, pres, str(fragment))
    add_tossup_answer(current_slide, pres, tossup["answer"])

def add_bonus_slides(pres, header: str, bonus: dict):
    """
    Adds the expanded slides for a bonus to the presentation
    """
    bonus_key_order = ["lead-in", "question-1", "answer-1", "question-2", "answer-2", "question-3", "answer-3"]
    current_slide = add_new_question(pres, header)
    for key in bonus_key_order:
        current_slide = add_question_fragment(current_slide, pres, bonus[key] + '\n')

def generate(tossups: list, bonuses: list, output_name):
    """
    Generates an expanded powerpoint for a packet with the given tossups and bonuses
    """
    pres = Presentation(PACKET_TEMPLATE)
    if len(tossups) != len(bonuses):
        print("Unequal number of tossups and bonuses")
        return
    for i in range(len(tossups)):
        add_tossup_slides(pres, TOSSUP_SLIDE_HEADER + str(i+1), tossups[i])
        add_bonus_slides(pres, BONUS_SLIDE_HEADER + str(i+1), bonuses[i])
    if ".pptx" not in output_name:
        output_name += ".pptx"
    pres.save("../output/" + output_name)
    