n = int(input("Введите число: "))
string = ""
while n != 0:
    string = str(n%2) + string
    n = n // 2
print(string)