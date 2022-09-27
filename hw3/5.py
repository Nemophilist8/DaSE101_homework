import random
def f(x):
    return x**3+x**2
N=1000000
C=0
S=(1-0)*(2-0)
for i in range(N):
    x=random.uniform(0,1)
    y=random.uniform(0,2)
    if 0<=y<=f(x):
        C+=1
    elif f(x)<=y<=0:
        C-=1
I=C/N*S
print(I)