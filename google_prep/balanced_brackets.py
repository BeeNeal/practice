

def is_balanced(s):

    closed_to_open = {'}': '{', '>': '<', ')': '(', ']': '['}
    seen = []

    for b in s:
        if b in set(closed_to_open.values()):
            seen.append(b)
        elif b in closed_to_open:
            if seen == []:
                return "No"
            elif seen[-1] == closed_to_open.get(b):
                seen.pop()
            else:
                return "No"

    if seen == []:
        return "Yes"
    return "No"




def is_balanced(s):

    closed_to_open = {'}': '{', '>': '<', ')': '(', ']': '['}

    seen = []  # my stack

    for char in s:
        if char in set(closed_to_open.values()):
            seen.append(char)
        elif char in closed_to_open:
            if seen == []:
                return False   # would be a closed bracket without an opener
            elif seen[-1] == closed_to_open.get(char):
                seen.pop()
            else:
                return False
    if seen == []:
        return True
    return False