#unique in given list
a=[1,2,3,4,4,4]
def uni(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for key,value in d.items():
        if value==1:
            print(key)

uni(a)

#given no is prime or not
print("enter number:")
c=int(input())
def isprime(c):
    if c<=1:
        return False
    for i in range(2,c):
        if c%i==0:
            return False
    return True
    
print(isprime(c))

#count vowels in a string

v={'a','e','i','o','u'}
s='abced'
def vowel(s):
    count=0
    for i in s:
        if i in v:
            count+=1
    return count
print("no of vowels:",vowel(s))



def func(s):
    l=[]
    for i in range(65,91):
        l.append(chr(i))
    count=0
    for i in s:
        count+= 1+l.index(i)
    return count
print(func('ABC'))

v={'a','e','i','o','u'}
def func(s):
    a=''
    for i in s:
        if i in v:
            
            a+=chr(ord(i)-32)

        else:
            a+=i
    return a
print(func('abceik'))

def func(s):
    a=''
    for i in s:
        if ord(i)>64 and ord(i)<96:
            a+=chr(ord(i)+32)
        else:
            a+=chr(ord(i)-32)
    return a
print(func("AbDf"))


def fun(a,b):
    new=''
    n=min(len(a),len(b))
    res=''
    for i in range(n):
        res+=a[i]
        res+=b[i]
    if len(a)>len(b):
        new+=a[n:]
        for x in new:
            res+=chr(ord(x)-32)
    else:
        new+=b[n:]
        for x in new:
            res+=chr(ord(x)-32)
    print(res)
fun('abcd','jk')

def sub(a,b):
    if b in a :
        return True
    else:
        return False
print(sub('abcd','ad'))

def cir(a,b):
    r=a+a
    print(b in r)
cir('abcd','cda')

3a4b= aaabbbb , 12a3d234c , 12abc3as4s

def first(s):
    for i in range (0,len(s),2):
        n=int(s[i])
        for j in range (n):
            print(s[i+1],end="")
first('3a4b5c') 

def second(s):
    num=""
    res=""
    for i in s:
        if i.isdigit():
            num+=i
        else:
            res+=int(num)*i
            num=""
    return res
print(second("10a11b"))

def third(s):
    res=""
    num=""
    a=""
    i=0
    while i<len(s):
        while s[i].isdigit():
            num+=s[i]
            i+=1
        while i<len(s) and s[i].isalpha():
            a+=s[i]
            i+=1
        res+=int(num)*a
        a=""
        num=""
    return res
print(third("10ab3cd"))
    

        

    
        

    



