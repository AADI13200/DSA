def max_consecutive(a):
    max,count=0,0
    for i in range(len(a)):
        if a[i]==1:
            count+=1

        else:
            count=0
        

        #using conditional expression and max will be changed once after the upper if else block is completed
        #if count > max then max will be count else max will be max itself
        max=count if count>max else max

    print("The maximum consecutive 1's are : ",max)


a=[1,1,0,1,1,1,0,1]
max_consecutive(a)  