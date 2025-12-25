#задание 1
with open('example.txt', 'r') as file:
    content = file.read()

#задание 2

text1 = input("")
with open('user_input.txt', 'w') as file:
    text1 = file.write(text1)

text2 = input("")
with open('user_input.txt', 'a') as file:
    text2 = file.write("\n" + text2)
#Задание 3
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('файл example.txt не найден')

try:
    with open('example.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print('файл example.txt не найден')