def longest_consecutive(a):
    cnt=1
    for i in a:
        if i+1 in a:
            cnt+=1
        print(i,"and count is",cnt)
    return cnt

a=[100, 4, 200, 1, 3, 2]
print(longest_consecutive(a))
