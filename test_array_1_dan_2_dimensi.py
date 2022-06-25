#author : Kurnia Raihan Ardian

#looping biasa
#i = 1
#while i<=5:
#    print(i)
#    i - 1

#array 2 dimensi
import math
from re import U


j=1
while j<=5:
    i = 1
    while i<=3:
        print([(j-1)*3+i],[i,j], end=" ")
        i = i + 1
        print()
    j += 1
print("\n")
print("Soal no 17")
j=1
while j<=5:
        i = 1
        while i<=3:
            print([i,j],i + (j-1)*3, end=" ")
            i +=1
            print()
        j += 1
print("\n")
print("Soal no 17 new version")
j=1
while j<=5:
        i = 1
        while i<=3:
            print([(j-1)*3+i],[i,j], end=" ")
            i +=1
            print()
        j += 1
print("\n")

n=1
j=1
while j<=5:
        i = 1
        while i<=3:
            print([i,j], end=" ")
            n += 1
            i += 1
            print()
        j += 1
print("\n")
i=1
while i<=3:
    j = i
    while j<=5:
        print([i,j], end=" ")
        j = j + 1
        print()
    i += 1
print("\n")
#Soal No 4
print("Mencetak hasil utang")
u = 1000000
i=1
j=u
while i<=11:
        b = j*0.02
        j=j+b
        c = j*0.1
        j = j-c
        print([i],[j],[b],[c])
        i += 1
print("\n")
#Soal No 4
print("Mencetak Soal No 4")
i=1
while i<=3:
    j = 1
    while j<=5:
        print([i,j], i + (j-1)*3, end=" ")
        print()
        j = j + 1
    i += 1
print("\n")
print("Mencetak Soal No 4")
i=1
while i<=3:
    j = 1
    while j<=5:
        print([i], i + (j-1)*3, end=" ")
        print()
        j = j + 1
    i += 1
print("\n")
#looping array 1 dimensi
i=1
while i<=10:
    print([i], end="")
    i += 2
print("\n")
n=10
i=1
while i<=10:
    print([n], end="")
    n = n - 1
    i += 1
print("\n")
i=1
while i<=10:
    print([67], end="")
    i += 2