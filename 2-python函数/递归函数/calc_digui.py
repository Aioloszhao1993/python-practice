def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def fact1(num, product):
    if num == 1:
        return product
    return fact1(num - 1, num * product)

if __name__ == "__main__":
    print(fact(5))
    # print(fact(1000))
    print(fact1(5, 1))
    # print(fact1(1000, 1))