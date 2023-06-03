from functional import create # функция создания файла "phone_book.txt"
from interface import interface # наш интерфейс в терминале
path = "phone_book.txt"
create(path) # функция создания файла "phone_book.txt"
enter = 0
while enter != 4:
    enter = interface()
    if enter == 1:
        from functional import add_cont # функция добавления контакта
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka) # функция добавления контакта
    elif enter == 2:
        from functional import show_all # функция вывода всех контактов
        print(show_all(path)) # функция вывода всех контактов
    elif enter == 3:
        from functional import search # функция поиска по фамилии
        stroka = str(input("Введите фамилию "))
        search(path, stroka) # функция поиска по фамилии
    elif enter == 5:
        from functional import remove # функция удаления контакта
        stroka = str(input('Введите фамилию для удаления: '))
        remove(path, stroka) # функция удаления контакта
    elif enter == 6: 
        from functional import edit # функция изменения контакта
        edit(path) # функция изменения контакта


print("спасибо за работу")