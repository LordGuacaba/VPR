from typeParsers.txtParser import *
from typeParsers.docxParser import get_tossups_and_bonuses as get_from_docx
from typeParsers.formatter import format_tossups, format_bonuses
from generator.generator import generate
from docx import Document
import sys, getopt

def get_questions_by_file_type(filepath: str) -> tuple:
    """
    Returns a (tossups, bonuses) tuple of question sets based on the packet's file type.
    """
    extension = filepath.split(".")[-1]
    if extension == "txt":
        return get_tossups_and_bonuses(filepath)
    elif extension == "docx":
        return get_from_docx(filepath)

def main(argv):
    input_file = ""
    output_file = ""
    opts, args = getopt.getopt(argv,"i:o:e")
    for opt, arg in opts:
        if opt == "-i":
            input_file = arg
            if "/" not in input_file:
                input_file = "../input/" + input_file
        elif opt == "-o":
            output_file = arg
        elif opt == "-e":
            insert_newlines(input_file)
    if input_file == "":
        print("Please specify an input file")
        return
    elif output_file == "":
        output_file = "expanded.pptx"
   
    try:
        tossups, bonuses = get_questions_by_file_type(input_file)
    except(TypeError):
        print("Unsupported file type")
        return
    tossups = format_tossups(tossups)
    bonuses = format_bonuses(bonuses)

    generate(tossups, bonuses, output_file)
    print("ALL DONE COWABUNGA")

if __name__ == "__main__":
    main(sys.argv[1:])