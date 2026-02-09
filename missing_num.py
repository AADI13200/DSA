def missing_num(a):
    for i in range(len(a)):
        if i not in a:
            print("The missing number is : ",i)


a=[1,2,3,5,6,7]
sol=missing_num(a)

