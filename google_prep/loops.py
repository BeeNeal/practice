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