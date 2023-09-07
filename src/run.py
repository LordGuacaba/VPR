from typeParsers.txtParser import *
from generator.generator import generate
import sys, getopt

def main(argv):
    input_file = ""
    output_file = ""
    opts, args = getopt.getopt(argv,"i:o:")
    for opt, arg in opts:
        if opt == "-i":
            input_file = arg
            if "/" not in input_file:
                input_file = "../input/" + input_file
        elif opt == "-o":
            output_file = arg
    if input_file == "":
        print("Please specify an input file")
        return
    elif output_file == "":
        output_file = "expanded.pptx"
    
    tossups, bonuses = get_tossups_and_bonuses(input_file)
    generate(tossups, bonuses, output_file)
    print("ALL DONE COWABUNGA")

if __name__ == "__main__":
    main(sys.argv[1:])