for i in range(101):
    t = "процент"
    ta = "процента"
    ov = "процентов"

    if i % 10 == 0:
        print(i, ov)
    elif 11 <= i < 21:
        print(i, ov)
    elif i % 10 == 1:
        print(i, t)
    elif 2 <= i % 10 < 5:
        print(i, ta)
    elif 5 <= i % 10 < 10:
        print(i, ov)
