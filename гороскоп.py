print("Как вас зовут?")
n=input("Введите своё имя,")
print("Ваша фамилия?")
n=input("Введите вашу фамилию,")
print("Ваше отчество?")
n=input("Введите своё отчество,")
correct_choice=False
while not correct_choice:
    choice = input("Напишите ваш пол м або ж ")
    if choice == 'м' or choice == 'ж':
        correct_choice = True
    else:
        print("Не правильно введён пол,повторите ввод, ")
print("Введите вашу дату рождения")
mon = int(input("Месяц"))
day = int(input("День"))
if mon == 1 and 22<day<31 or mon == 2 and 1<day<19:
    print ("Вы по гороскопу......!")
elif mon == 2 and 20<day<31 or mon == 3 and 1<day<20:
    print ("Вы по гороскопу......!")
elif mon == 3 and 21<day<31 or mon == 4 and 1<day<20:
    print ("Вы по гороскопу......!")
elif mon == 4 and 21<day<31 or mon == 5 and 1<day<22:
    print ("Вы по гороскопу......!")
elif mon == 5 and 23<day<31 or mon ==  6 and 1<day<22:
    print ("Вы по гороскопу......!")
elif mon == 6 and 23<day<31 or mon == 7 and 1<day<22:
    print ("Вы по гороскопу......!")
elif mon == 7 and 22<day<31 or mon == 8 and 1<day<22:
    print ("Вы по гороскопу......!")
elif mon == 8 and 22<day<31 or mon == 9 and 1<day<23:
    print ("Вы по гороскопу......!")
elif mon == 9 and 22<day<31 or mon == 10 and 1<day<23:
    print ("Вы по гороскопу......!")
elif mon == 10 and 22<day<31 or mon == 11 and 1<day<23:
    print ("Вы по гороскопу......!")
elif mon == 11 and 22<day<31 or mon == 12 and 1<day<23:
    print ("Вы по гороскопу......!")

