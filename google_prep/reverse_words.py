def reverse_words(sentence):

    words = []
    word_start = len(sentence)
    word_end = 0
    for i in xrange(1, len(sentence) + 1):
        if i == len(sentence):
            words.append(sentence[0:word_end])

        elif sentence[-i] == ' ':
            word_end = -i
            words.append(sentence[word_end:word_start])
            word_start = -i

    return words

