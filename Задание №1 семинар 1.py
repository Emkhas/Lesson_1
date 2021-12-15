# Пркедставлены два варианта верешия задания №1
# variant_1

duration = int(input("Расчет производится способом №1. Введите продолжительность времени в секундах (не более 86400 сек): "))
if duration <= 59:
    print(duration, "сек")
elif 60 <= duration < 3600 and duration % 60 == 0:
    min_a = duration // 60
    print(min_a, "мин")
elif 60 <= duration < 3600:
    min_a = duration // 60
    min_b = duration % 60
    print(min_a, "мин", min_b, "сек")
if 3600 <= duration < 86400 and duration % 3600 == 0:
    hour = duration // 3600
    print(hour, "час")
elif 3600 <= duration < 86400:
    hour_a = duration // 3600
    hour_b = duration % 3600
    if 0 <= hour_b <= 59:
        print(hour_a, "час", hour_b, "сек")
    elif 60 <= hour_b <= 3599 and hour_b % 60 == 0:
        print(hour_a, "час", hour_b // 60, "мин")
    elif 60 <= hour_b <= 3599:
        print(hour_a, "час", hour_b // 60, "мин", hour_b % 60, "сек")

# variant_2
duration = int(input("Расчет производится способом №2. Введите продолжительность времени в секундах: "))

days = duration // (60 * 60 * 24)
hours = (duration - days * (60 * 60 * 24)) // (60 * 60)
minutes = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
seconds = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60
print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
