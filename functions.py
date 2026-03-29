def cal(num):
    if num % 2 == 0:
        total = 0
        for i in range(1, num+1):
            if i % 2 == 0:
                total += i
        return total
    else:
        product = 1
        for i in range(1, num+1):
            if i % 2 != 0:
                product *= i
        return product

print(cal(5))