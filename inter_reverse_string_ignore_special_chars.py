def rev_string_ignore_special_chars(s):
    slist = list(s)
    new =""
    findex = 0
    bindex =len(s)-1
    while findex<bindex:
        if not slist[findex].isalpha():
            findex+=1
        elif not slist[bindex].isalpha():
            bindex-=1
        else:
            slist[findex],slist[bindex] = slist[bindex],slist[findex]
        findex+=1
        bindex-=1
        ret = (''.join(slist))
    return (ret)
s = 'a#bc/de'
print(rev_string_ignore_special_chars(s));