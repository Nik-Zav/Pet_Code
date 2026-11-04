def gip_kollatsa():
    n = int(input("Введите число: "))
    b = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            b += 1
        else:
            n = n * 3 + 1
            b += 1
    print(b)

if __name__ == '__main__':
    gip_kollatsa()
