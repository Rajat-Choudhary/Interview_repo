def long_word(n,string):
    word_len = []
    txt = string.split(" ")
    for i in txt:
        if len(i) > n:
            word_len.append(i)
    return word_len

print(long_word(3, "The quick brown fox jumps over the lazy dog"))