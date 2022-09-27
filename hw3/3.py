s="abccccdaaaaaaaaaaa"
l=1
max=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        l+=1
        if l>max:
            max=l
    else:
        l=1
print(max)
