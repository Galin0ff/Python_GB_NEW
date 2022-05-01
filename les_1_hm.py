'''
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
'''

sec = int(input('Ввведите число: '))

sec = sec % (24 * 3600)
hour = sec // 3600
sec %= 36001
minu = sec // 60
sec %= 60
print("Часов:", hour)
print("Минут:", minu)
print("Секунд:", sec)

print(f"{hour}:{minu}:{sec}\n")


'''
Создать список, состоящий из кубов нечётных чисел от 0 до 1000
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
 делится нацело на 7
'''

print('Задача №2')

def in_sum(n, sum_dig):
    if n > 0:
        sum_dig += n % 10
        n = n // 10
        return(in_sum(n, sum_dig))
    else:
        return sum_dig

list_of_dig = []
sum1 = 0
sum2 = 0

for i in range(100):
    list_of_dig.append(i*i*i)
    if (in_sum(list_of_dig[i], 0) % 7) == 0:
        sum1 += in_sum(list_of_dig[i], 0)
    list_of_dig[i] += 17
    if (in_sum(list_of_dig[i], 0) % 7) == 0:
        sum2 += in_sum(list_of_dig[i], 0)

print(sum1)
print(sum2,'\n')
#print(list_of_dig)

'''
Реализовать склонение слова «процент» для чисел до 20. Например, 
задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». 
Вывести все склонения для проверки.
'''
print('Задача №3')

list_of_str = ['процент', 'процента', 'процентов']
list_of_dig = []

for i in range(1, 21):
    list_of_dig.append(i)
    if i == 1:
        print(list_of_dig[i-1], list_of_str[0])
    elif (i > 0) and (i < 5):
        print(list_of_dig[i-1], list_of_str[1])
    else:
        print(list_of_dig[i-1], list_of_str[2])