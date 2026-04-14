a=[1,2,3,4,5,5,6,5,9]
b=[5,6,7,8,9,10]
s=[]

for i in a:
    if i not in s:
        s.append(i)
for j in b:
    if j not in s:
        s.append(j)
print("Union of a and b is : ",s)