n = int(input("Digite um número inteiro: "))


x, y = 0, 1

while x <= n:
    print(x, end=" ")
    x, y = y, x + y