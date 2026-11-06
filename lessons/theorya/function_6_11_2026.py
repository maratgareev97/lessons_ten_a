def perevod_in_five_system(a):
    s=""
    while a>0:
        ost=a%5
        a=a//5
        s+=str(ost)
    s=s[::-1]
    return s

def my_summa(a,b):
    trash="Вася"
    return a+b,trash

rez = perevod_in_five_system(5654443)
print(rez)


print(my_summa(56,87))




