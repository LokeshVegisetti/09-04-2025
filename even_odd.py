    
num=[2,1,3,4,5,6,78,85,3]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)