#Получить с клавиатуры 6 чисел.
#Вывести на экран их в возрастающем порядке


a = []
print('!!!введите 6 целых чисел!!!!')

for i in range (0, 6):
	b = int(input())
	a.append(b)
	a.sort()

print(a)
