# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# import os 

def add_person():
    last_name = input ('Введите фамилию: ')
    name = input ('Введите имя: ')
    surname = input ('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    data = open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'a', encoding='utf-8')
    data.writelines([last_name, ' ', name, ' ',surname, ' ',phone, '\n '])
    data.close()

def print_data():
   with open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'r', encoding='utf-8') as data:
       print(data.read())

def search():
    search_name = input('Введите данные: ')
    with open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

def load_data():
    with open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'r+', encoding='utf-8') as data:    
        text_data = data.read()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line not in text_data:
                    data.write(line) 

def delete_data(): #удаление данных
    del_name = input ('Введите контакт, который нужно удалить: ')
    with open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'r', encoding='utf-8' ) as data:
        del_data = data.readlines()
        for i_line in range(len(del_data)):
            if del_name in del_data[i_line]:
                del_data[i_line]
    with open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'w', encoding='utf-8' ) as data:
        print(del_data)
        for line in del_data:
            data.write(line)
                              
def change_data(): #изменение данных
    change_inf = input('Введите данные, которые необходимо изменить: ')
    last_name = input ('Введите корректную фамилию: ')
    name = input ('Введите корректное имя: ')
    surname = input ('Введите корректное отчество: ')
    phone = input('Введите корректный номер телефона: ')    
    with open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'r', encoding='utf-8' ) as data:
        changes = data.readlines()
    for i_line in range (len(changes)):
        if change_inf in changes[i_line]:
            changes[i_line] = last_name + ' ' + name + ' ' + surname + ' ' + phone      
    with open('C:\\Users\\Admin\\Desktop\\Python Seminars\\Seminar_8\\Files8\\phonebook.txt', 'w', encoding='utf-8' ) as data:
        for line in changes:
            data.write(line)

def ui():
    # os.system('cls')
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удаление данных
6 - изменение данных''')
    user_input = input ('Введите нужный вариант: ')
    if user_input == '1':
        add_person()
    elif user_input == '2':
        search()
    elif user_input == '3':
        load_data()
    elif user_input == '4':
        print_data()
    elif user_input == '5':
        delete_data()
    elif user_input == '6':
        change_data()

print_data()

        # os.system('cls')
#         print('''1 - добавить контакт
# 2 - поиск
# 3 - импорт данных
# 4 - вывод в консоль
# 5 - удаление данных
# 6 - изменение данных''')
        # user_input = input ('Введите нужный вариант: ')

def main():
    ui()
    
if __name__ == '__main__':
    main()
