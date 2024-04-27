def isort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
l=[100,25,58,6,32,17]
print("before sorted",l)
isort(l)
print("after sorting",l)




