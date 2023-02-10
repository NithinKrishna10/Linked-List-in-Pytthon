def func(x):
    return 0 if x == 0 else x + func(x - 1)

print(func(4))