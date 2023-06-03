# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .tstrokat.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии
# from func import *
# privet()

# 1 - Интерфейс (то что общается с пользователем: введите данные, что вы хотите, меню, сохранить?)
# 2 - работа с файлом (файл, где лежат функции записи, сохранения и чтения)
# 3 - алгоритм(в начале приветствие и выбор из интерфейса)

# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход
#path ='phone book.tstrokat' # создали текстовый файл который называется phone book.tstrokat и положили его в переменную path
def create(path): # функция создания файла "phone_book.tstrokat"
    try: # если файл уже есть то мы открываем его
        file = open(path, 'r') # file - переменная с которой мы работаем. открыли файл для чтения
    except IOError: # если файла нет то мы его создаем
        print('Создан новый справочник -> phone_book.tstrokat ')
        file = open(path, 'w') # file - переменная с которой мы работаем. открыли файл для записи
    finally: # закрываем файл
        file.close()


def add_cont(file_name, stroka): # функция добавления контакта
    data = open(file_name, 'a') # data - переменная с которой мы работаем. открыли файл для записи
    data.write(stroka + "\n")
    data.close()

def show_all(file_name): # функция вывода всех контактов
    data = open(file_name, "r") # data - переменная с которой мы работаем.открыли файл для чтения
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, stroka): # функция поиска по фамилии
    a = 0
    data = open(file_name, 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("нет такого")
    data.close()


def remove_contact(file_name, stroka): # функция удаления контакта
    with open(file_name, 'r') as open_book:
        lines = open_book.readlines()
        with open(file_name, 'w') as open_book:
            for line in lines:
                if stroka in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    open_book.write(line)

def edit(file_name):
    with open(file_name, 'r+') as open_book:
        search_param = (input('Введите параметр для поиска: ' ).title())
        lines = open_book.readlines()
        open_book.seek(0)
        for line in lines:
            if search_param in line:
                print(line)
                add_i = (input('Введите Имя: ' ).title())
                add_tel = (input('Введите телефон: ' ).title())
                new_line = add_i +' '+ add_tel + '\n'
                line = line.replace(line, new_line)
            open_book.write(line)
        open_book.truncate()