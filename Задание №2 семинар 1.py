my_list = []  # Создаем список
for num in range(1, 1001, 2):
    my_list.append(num ** 3)  # Возводим в степень 3
print(my_list)

sum_a = 0
for num in my_list:
    sum_b = 0
    for num_a in str(num):
        sum_b += int(num_a)
    if sum_b % 7 == 0:
        sum_a += num
print(sum_a)

sum_a = 0
for num in my_list:
    num += 17
    sum_b = 0
    for num_a in str(num):
        sum_b += int(num_a)
    if sum_b % 7 == 0:
        sum_a += num
print(sum_a)
