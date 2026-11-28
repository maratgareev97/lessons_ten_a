n=11
s=''
while n>0:
    o = n%3
    n = n//3
    s+=str(o)
s=s[::-1]
print(s)

#--------------------------
n='102112'
z=n[:len(n)//2:]
a=n[len(n)//2::]
print(z+'9'+a)

