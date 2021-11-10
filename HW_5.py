lst = [3, 7, 2, 8, 9, 2, 2, 6, 4, 100]
i = []
k = 0
for i in range(1, len(lst)-1):
 if lst[i - 1] < lst[i] > lst[i + 1]:
  k += 1
  print(f"элементы, которые больше своих сосдеей {lst[i]}")
print(f"колличество елементов {k}")

spisok = input('рост учеников в школе').split()
Petya = input('рост Petya')
spisok.append(Petya)
spisok = sorted(spisok, reverse=True)
print(spisok)
print(len(spisok) - spisok[::-1].index(Petya))

list_3 = [int(x) for x in input("Enter  list: ").split()]
k = int(input("Enter  k: "))
for i in range(k+1, len(list_3)):
    list_3[i - 1] = list_3[i]
list_3.pop()
print(list_3)







