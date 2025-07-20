
# missing positive
def miss(a):
    for i in range(1,max(a)):
        if i not in a:
            print(i)
miss([1,3,4])

#move zeros to last
def zero(a):
    n=[]
    z=[]
    for i in a:
        if i==0:
            z.append(i)
        else:
            n.append(i)
    return n+z
print(zero([1,2,0,3,4,0,5,6,0]))
 
#move even to last 
def even(a):
    n=[]
    e=[]
    for i in a:
        if i%2==0:
            e.append(i)
        else:
            n.append(i)
    return n+e
print(even([1,2,3,4,5,6]))

def fun(a):
    n=len(a)
    for i in range(0,n//2):
        if a[i]==0:
            a[i],a[n-i]=a[n-i],a[i]
    return a
print(fun([1,2,0,4,3,5,0]))

def sol(a):
    for i in a:
        if i==0:
            a.remove(i)
            a.append(i)
    return a 
    
def sol2(a):
    for i in a:
        if i%2==0:
            a.remove(i)
            a.append(i)
    return a 
print(sol([1,3,0,0,4,0,2]))
print(sol2([1,3,6,4,5,8]))  

def two(a):
    k=0
    i=0
    for i in range(len(a)):
        if a[i]%2!=0:
            temp=a.pop(i)
            a.insert(k,temp)
            k+=1
    return a 
print(two([1,3,6,4,5,8]))  


def bit(a):
    count=0
    while a>0:
        r=a%2
        if r!=0:
            count+=1
        a=a//2
    print(count)
bit(1245)








