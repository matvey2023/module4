
spisok=[]

kolichestvo_chisel=int(input("Сколько чисел в списке? "))

for i in range(kolichestvo_chisel):
    chislo=int(input("Введите число: "))
    spisok.append(chislo)

ind=0
for k in range(kolichestvo_chisel-1):
    a=spisok[ind]
    indx = ind + 1
    for k in range(kolichestvo_chisel-ind-1):
        b=spisok[indx]
        if a>b:
            spisok[ind], spisok[indx]=spisok[indx], spisok[ind]
        indx=indx+1
    ind = ind + 1
# indx=0
# for i in range(kolichestvo_chisel-1):
#     a=min(spisok[indx:])
#     povtor=spisok.count(a)
#     for i in range(povtor):
#         spisok[spisok.index(a)], spisok[indx] = spisok[indx], spisok[spisok.index(a)]
#     indx=indx+1
print(spisok)
