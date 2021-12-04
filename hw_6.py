print(len(set(input("Enter  list: ").split())))
print(len(set(input("Enter  list1:").split()) & set(input("Enter  list2:").split())))

words = input("Enter words: ").split()
result = {}
for word in words:
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1
for word, value in result.items():
 print(f'Слово: {word}, Количество: {value}')

counter = {}
for i in range(int(input("Выбери сколько будет списков"))):
    line = input("го списки").split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(f'слово, которе больше всего встретилось {most_frequent[-1]}')


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for n in range(2, n):
        if n % n ==0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Введите число, чтобы узнать простое оно или нет: "))
    if not is_prime(n):
        print("Составное число")
    else:
        print("Простое число")

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
print(power(float(input("Введите число: ")), int(input("Введите степень числа: "))))

a = int(input("Введите число, чтобы найти общий делитель: "))
b = int(input("Введите второе число, чтобы найти общий делитель: "))
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
gcd = a + b
print(gcd)

a = int(input('Пиши, а наименьшее общее кратное двух чисел'))
b = int(input('Пиши, b наименьшее общее кратное двух чисел'))

p = a * b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
gcd = a + b
lcm = p // gcd
print ("наименьшее общее кратное двух чисел",lcm)

