def format_tossups(tossups: str) -> list:
    """
    Given a string containing all tossup lines in a packet, returns
    a list where each item is a tossup and its answer.
    """
    tossup_list = list()
    tossup_lines = tossups.split('\n')
    current_tossup = dict()
    current_tossup["power"] = ""
    is_in_power = True
    is_answer_line = False
    for line in tossup_lines:
        if is_answer_line:
            if starts_with_number(line):
                if len(current_tossup) != 0:
                    tossup_list.append(current_tossup)
                    current_tossup = dict()
                current_tossup["power"] = remove_bad_stuff(line)
                is_answer_line = False
                is_in_power = True
            else:
                current_tossup["answer"] += remove_bad_stuff(line)
        else:
            if not is_in_power and line[:7].lower() == "answer:":
                is_answer_line = True
                current_tossup["answer"] = remove_bad_stuff(line) 
            elif is_in_power:
                if "(*)" in line:
                    pow_split = line.split("(*)")
                    current_tossup["power"] += remove_bad_stuff(pow_split[0]) + "(*)"
                    current_tossup["non-power"] = remove_bad_stuff(pow_split[1])
                    is_in_power = False
                else:
                    current_tossup["power"] += remove_bad_stuff(line)
            else:
                current_tossup["non-power"] += remove_bad_stuff(line)
    if len(current_tossup) != 0:
        tossup_list.append(current_tossup)
    return tossup_list

def format_bonuses(bonuses: str) -> list:
    """
    Given a string containing all bonus lines in a packet, returns
    a list where each individual item is a single bonus set.
    """
    bonus_list = list()
    bonus_lines = bonuses.split('\n')
    current_bonus = dict()
    current_field = "lead-in"
    for line in bonus_lines:
        if line[:3] == "[10":
            current_field = "question-" + str((len(current_bonus) + 1) // 2)
            current_bonus[current_field] = remove_bad_stuff(line)
        elif line[:7].lower() == "answer:":
            current_field = "answer-" + str(len(current_bonus) // 2)
            current_bonus[current_field] = remove_bad_stuff(line)
        elif starts_with_number(line):
            if len(current_bonus) > 0:
                bonus_list.append(current_bonus)
            current_bonus = dict()
            current_field = "lead-in"
            current_bonus[current_field] = remove_bad_stuff(line)
        else:
            current_bonus[current_field] += remove_bad_stuff(line)
    if len(current_bonus) > 0:
        bonus_list.append(current_bonus)
    return bonus_list
            

def remove_bad_stuff(line: str) -> str:
    """
    Removes the following from tossup or bonus lines
    - moderator notes
    - numbering
    - "ANSWER:"
    - pronunciation guides
    - author notes
    """
    if len(line) == 0:
        return ""
    try:
        if line[:14].lower() == "moderator note" or line[:17].lower() == "note to moderator":
            return ""
    except:
        pass
    if starts_with_number(line):
        line = line[3:].strip()
        return line + '\n'
    if line[:3] == "[10":
        return line[line.find("]"):] + '\n'
    try:
        if(line[0:7].lower() == "answer:"):
            return line[7:].strip() + '\n'
    except:
        pass
    if '(“' in line:
        start = line.find('(“')
        if '”)' in line:
            end = line.find('”)') + 2
            return line[:start-1] + line[end:] + '\n'
        else:
            return line[:start] + '\n'
    elif '”)' in line:
            end = line.find('”)') + 2
            return line[end:] + '\n'
    if line[0] == "<" and line[-1] == ">":
        return ""
    return line + '\n'

def starts_with_number(line: str) -> bool:
    """
    Returns true if the given line starts with a number, false otherwise.
    """
    try:
        int(line[0])
        if line[1] == '.' or line[2] == '.':
            return True
        else:
            return False
    except:
        return False