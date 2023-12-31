"""
Provides a set of functions that directly interact with the PowerPoint presentation being generated.

Author: Will Hoover
"""

# Tossup Utils

def duplicate_tossup_slide(slide, pres):
    """
    Adds and returns a duplicate of the last slide in the given presentation.
    """
    template = slide
    blank_slide_layout = pres.slide_layouts[1]

    copied_slide = pres.slides.add_slide(blank_slide_layout)
    copied_slide.shapes.title.text = template.shapes.title.text
    copied_slide.shapes[1].text_frame.paragraphs[0].text = template.shapes[1].text_frame.paragraphs[0].text
    question_box = copied_slide.shapes[1].text_frame.paragraphs[0]
    question_box.add_run()
    question_box.add_run()
    question_box.runs[0].text = template.shapes[1].text_frame.paragraphs[0].runs[0].text
    question_box.runs[1].text = template.shapes[1].text_frame.paragraphs[0].runs[1].text
    question_box.runs[0].font.bold = True
        
    copied_slide.name = f'{slide}'

    return copied_slide

def add_new_tossup_question(pres, header: str):
    """
    Adds a new slide that is the start of the next tossup or bonus. This slide will be duplicated to
    create further slides for this question.
    Returns the slide that was created.
    """
    new_slide = pres.slides.add_slide(pres.slide_master.slide_layouts[1])
    new_slide.shapes.title.text = header
    question_box = new_slide.shapes[1].text_frame.paragraphs[0]
    question_box.add_run()
    question_box.add_run()
    question_box.runs[0].font.bold = True
    return new_slide

def add_tossup_fragment(prev_slide, pres, fragment: str, power: bool = False):
    """
    Creates and adds a new slide with the given question fragment appended to it.
    Returns the slide that was created.
    """
    run_index = 1
    new_slide = duplicate_tossup_slide(prev_slide, pres)
    if power:
        run_index = 0
    new_slide.shapes[1].text_frame.paragraphs[0].runs[run_index].text += fragment
    return new_slide

def add_tossup_answer(prev_slide, pres, answer: str):
    """
    Creates and adds a new slide with the given answer to the finished tossup inserted at the bottom.
    Returns the slide that was created.
    """
    answer_allocation = '\n\n' + answer
    return add_tossup_fragment(prev_slide, pres, answer_allocation)

# Bonus Utils

def add_new_bonus_question(pres, header: str):
    """
    Adds a new slide that is the start of the next tossup or bonus. This slide will be duplicated to
    create further slides for this question.
    Returns the slide that was created.
    """
    new_slide = pres.slides.add_slide(pres.slide_master.slide_layouts[1])
    new_slide.shapes.title.text = header
    new_slide.shapes[1].text_frame.paragraphs[0].text = ""
    return new_slide

def duplicate_bonus_slide(slide, pres):
    """
    Adds and returns a duplicate of the last bonus slide in the given presentation.
    """
    template = slide
    blank_slide_layout = pres.slide_layouts[1]

    copied_slide = pres.slides.add_slide(blank_slide_layout)
    copied_slide.shapes.title.text = template.shapes.title.text
    copied_slide.shapes[1].text_frame.paragraphs[0].text = template.shapes[1].text_frame.paragraphs[0].text
        
    copied_slide.name = f'{slide}'

    return copied_slide

def add_bonus_fragment(prev_slide, pres, fragment: str):
    """
    Creates and adds a new slide with the given question fragment appended to it.
    Returns the slide that was created.
    """
    new_slide = duplicate_bonus_slide(prev_slide, pres)
    new_slide.shapes[1].text_frame.paragraphs[0].text += fragment
    return new_slide