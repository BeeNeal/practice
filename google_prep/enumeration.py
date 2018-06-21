def gen_all_seqs(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences for the outcomes
    of a given length
    """

    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
length = 2
seq_outcomes = gen_all_seqs(outcomes, length)
print seq_outcomes


def gen_sorted_seqs(outcomes, length):

    all_seqs = gen_all_seqs(outcomes, length)
    sorted_seqs = 