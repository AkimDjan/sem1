def maxunic(s):
    c=set()
    lev=0
    m=0
    for r in range(len(s)):
        while s[r] in c:
            c.remove(s[lev])
            lev+=1
        c|={s[r]}
        m=max(m,len(c))
    return m

print(maxunic(input()))