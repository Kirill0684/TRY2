a = int(input('Input number: '))
b = a % 10
c = 0
if a != 0:
    while b >= c:
        if b > c:
            c = b
        a = a // 10
        b = a % 10
else:
    print("0")
    break

print('Maximum digit: ', c)
