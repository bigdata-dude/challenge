def rev_words(s):
    words = s.split(" ")
    print(words)
    newWords = words[::-1]
    newSentence = ' '.join(newWords)
    return (newSentence)

s= 'This is a line'
res=(rev_words(s))
print(res)