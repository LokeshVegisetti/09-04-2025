num=[1,2,3,4,1,2,3,5,5,6,7,8,5,2,6]
unq=[]
for i in num:
    if  i not in unq:
        unq.append(i)

    else:
        unq.append('*')

print(unq)