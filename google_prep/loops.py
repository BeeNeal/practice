def has22(nums):
    try:
        first = nums.index(2)
    except:
        return False
    if first is not None:
        for i in xrange(first, len(nums) - 1):
            if nums[i] == 2 and nums[i + 1] == 2:
                return True
            else:
                continue
    return False


def sum_nums(s):

    total = 0

    for i in xrange(len(s)):
        amt_nums = 0
        if s[i].isdigit:
            current_pos = i
            amt_nums += 1
        elif not s[i].isdigit and current_pos:
            total += int(s[current_pos - amt_nums:current_pos])
            current_pos = None
            amt_nums = 0
        else:
            amt_nums = 0
    return total

    # 'this is a string'
    # start = 0
    # for i in s:
    #     if i.isdigit():
    #         start = i
    #     if i == ' ':
    #         chunk = 

import re

def sum_nums(s):

    total = 0
    nums = filter(None, re.split(r'(\d+)', s))
    for item in nums:
        if item.isdigit():
            total += int(item)

    return total