s=1
for i in range(1,101,2):
    print(i,end=" ")
    if i<50:
        s*=i
print("\n",s,sep="")
