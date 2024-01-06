# VPR
**V**isual **P**acket **R**eader is a Quiz Bowl packet parser that expands normal Quiz Bowl packets into PowerPoint presentations animated line by line, intended for deaf or hard of hearing players. The program will expand a standard quizbowl packet into a series of powerpoint slides. Tossup slides may be clicked through, adding on a phrase or sentence at a time as it is read out loud. Bonus slides display one bonus portion at a time. Answers to each are always displayed on the slide after their corresponding questions are complete.

## Contents
- [How To Use](#how-to-use)
- [What's New](#whats-new)
- [Planned Updates](#planned-updates)

## How To Use
### Prerequisites
- Python 3.x - [Download Python](https://www.python.org/downloads/)
- Ensure that you have [pip](https://pypi.org/project/pip/) installed
- [python-pptx](https://python-pptx.readthedocs.io/en/latest/index.html) - `pip3 install python-pptx`
### Steps to use
Ensure that you have VPR downloaded locally. Before using, place any input files (currently only .txt files are supported) in the `/input` directory. Next, open VPR in the command line and switch to the `/src` directory.
<br>
`cd src`
<br>
To run VPR, use the following command:
<br>
`python3 run.py -i <input_file> -o <output_file> -e`
<br>
Arguments:
- `-i` input file name. Can be either a full or relative path to the file or a file name in the form <name>.txt or <name>.docx that is in the `/input` directory
- `-o` (optional) output file name. The output file generated in the `/output` directory will have this name. The .pptx extension is not needed. Will default to "expanded.pptx" if not provided
- `-e` (optional) denotes that a file contains many tossups entirely on one line. The file will be expanded into ~100-character lines before it is processed.

## What's New
v0.3.0
- Input files can be word documents as well as .txt files

v0.2.0
- Power clues now show up in bold
  
v0.1.1
- Output PowerPoint no longer opens in slide master mode
- Text spacing improved
## Planned Updates
Features
- Precise bold/underline on answer lines (word doc input only)
- Local GUI (eventually)
Fixes
- Tighten pronunciation guide removal
- Code refactoring
- Cross-OS compatability checks
- Remove extra slide between end of tossup and answer
- Remove space between power mark and end of power
- Better error output during packet parsing
