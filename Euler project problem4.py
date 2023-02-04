s=[]
def multiple():
    m = i * a
    m = str(m)
    if m[0] == m[-1] and m[1] == m[-2] and m[2] == m[-3]:
        m=int(m)
        s.append(m)
for i in range(100,1000):
    for a in range(100,1000):
        multiple()
print('maxpalindrome=',max(s))
