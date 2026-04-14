def two_sum(a):
    target=int(input("Enter the target number: "))
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]==a[j]:
                continue
            if a[i]+a[j]==target:
                print("The two numbers that add up to the target are:",a[i],"and",a[j],"at indices",i,"and",j)



a=[1,2,3,4,5,6,7,8,9]
two_sum(a)