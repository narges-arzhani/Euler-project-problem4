s=[]
def multiple():
    m = i * a
    m = str(m)
    if m==m[::-1]:
        m=int(m)
        s.append(m)
for i in range(100,1000):
    for a in range(100,1000):
        multiple()
print('maxpalindrome=',max(s))
