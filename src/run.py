from typeParsers.txtParser import *

def main():
    insert_newlines("tmp/stuff.txt")
    tossups, bonuses = get_tossups_and_bonuses("tmp/stuff.txt")
    print(tossups[2])
    print(tossups[11])
    print(bonuses[5])
    print(bonuses[13])
    print(len(tossups))
    print(len(bonuses))

if __name__ == "__main__":
    main()