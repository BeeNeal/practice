

def merge_ranges(meeting_times):
    """Condenses meeting times

    >>> merge_ranges([(1, 3), (2, 3), (1, 4), (5, 6)])
    [(1, 4), (5, 6)]

    """

    meeting_times.sort()
    condensed = [meeting_times[0]]

    for start, end in meeting_times[1:]:
        last_merged_start, last_merged_end = condensed[-1]
        if start <= last_merged_end:
            condensed[-1] = (last_merged_start, max(end, last_merged_end))
        else:
            condensed.append((start, end))

    return condensed

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "You passed!"