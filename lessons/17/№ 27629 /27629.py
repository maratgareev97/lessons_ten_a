
file=list(map(int,open("17_27629.txt").readlines()))

print(len(file))
s=-1000000
s2 = -1000000
count = 0

for i in range(len(file)):
   if len(str(abs(file[i])))==4 and str(file[i])[-2:]=='43':
        if file[i]>s:
            s = file[i]
print(s)

for i in range(len(file)-1):
    k = 0
    if len(str(abs(file[i])))==4:
        k += 1
    if len(str(abs(file[i+1])))==4:
        k += 1
    if k>0:
        print(file[i],file[i+1])
        summa = file[i]+file[i+1]
        kvad = summa**2
        if kvad < s**2:
            count +=1
            if kvad>s2:
                s2 = kvad
print(count,s2)





