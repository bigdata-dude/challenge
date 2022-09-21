def reverStringsInLine(s):
    sl = s.split(' ')
    rsl = ''

    for word in sl:
        str_word = ''
        rev_sub_word = ''
        for ch in word:

            if ch.isalnum():
                str_word += ch
            else:
                rev_sub_word += str_word[::-1] + ch
                str_word = ''
        r_word = rev_sub_word + str_word[::-1]
        rsl += r_word + ' '
    return rsl

#s = 'Bangalore is@#$!123locked locked again in jul2020'
s = 'Bangal@#$!1'
print(reverStringsInLine(s))