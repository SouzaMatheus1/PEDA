def recursivamente_3(num):
    if num <= 0:
        return num
    else:
        return recursivamente_3(num - 1) + 3

print(recursivamente_3(5))