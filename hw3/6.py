# 法一
def way_1(c):
    x=c-1
    a=0.5
    def f(a,n):
        s=1
        for i in range(n):
            s*=(a-i)
            s/=(i+1)
        return s
    s=0
    for i in range(1000):
        s+=f(a,i)*(x**i)
    return s
print(way_1(2))
# 法二
def way_2(c):
    i=0
    g=0
    for j in range(c+1):
        if j*j>c and g==0:
            g=j-1
        while abs(g*g-c)>0.0001:
            g+=0.00001
            i+=1
    return g
print(way_2(2))
# 法三
def way_3(c):
    i=0
    m_max=c
    m_min=0
    g=(m_max+m_min)/2
    while abs(g*g-c)>0.00000001:
        if g*g<c:
            m_min=g
        else:
            m_max=g
        g=(m_max+m_min)/2
        i+=1
    return g
print(way_3(2))

