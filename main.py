from sub_repo.add import add


def calculator(x, y, func):
    return func(x, y)


print(calculator(2, 5, add))
