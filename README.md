# VPR
**V**isual **P**acket **R**eader is a Quiz Bowl packet parser that expands normal Quiz Bowl packets into PowerPoint presentations animated line by line, intended for deaf or hard of hearing players.

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
- `-i` input file name. Can be either a full or relative path to the file or a file name in the form <name>.txt that is in the `/input` directory
- `-o` (optional) output file name. The output file generated in the `/output` directory will have this name. The .pptx extension is not needed. Will default to "expanded.pptx" if not provided
- `-e` (optional) denotes that a .txt file contains many tossups entirely on one line. The file will be expanded into ~100-character lines before it is processed.

## What's New
This is the first usable version of VPR! Stay tuned for more updates.
## Planned Updates
TBD
