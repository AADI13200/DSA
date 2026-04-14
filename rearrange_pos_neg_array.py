# Brute force approach

def rearrange_array(a):
    pos=[]
    neg=[]

    for i in a:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)

    for i in range(len(a)//2):
        a[2*i]=pos[i]
        a[i*2+1]=neg[i]
    print(a)
a=[1,2,3,-4,-1,-9]
rearrange_array(a)

#optimal approach
def rearrange_array(a):
    pos_index=0
    neg_index=1
    ans=[0]*len(a)

    for i in a:
        if i<0:
            ans[neg_index]=i
            neg_index+=2
        else:
            ans[pos_index]=i
            pos_index+=2
    print(ans)

a=[1,2,3,-4,-1,-9]
rearrange_array(a)
