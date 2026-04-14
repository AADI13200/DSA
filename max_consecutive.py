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
        # mostly add this line in 1st if condition block but it will be executed in every iteration of the
        #  loop and we can avoid that by adding this line outside the if else block
    print("The maximum consecutive 1's are : ",max)


a=[1,1,0,1,1,1,0,1]
max_consecutive(a)  