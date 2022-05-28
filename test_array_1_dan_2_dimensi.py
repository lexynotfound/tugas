#author : Kurnia Raihan Ardian

#looping biasa
#i = 1
#while i<=5:
#    print(i)
#    i - 1

#array 2 dimensi
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