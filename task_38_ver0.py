'''
Задача 38:
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных
'''


phone_book = '/run/media/evgeny/My_storage/01_DATA/Обучение GeekBrains/Work/PYTHON_intro/08_Seminar/phone_book.txt'


def program_menu() -> int:
    print("\nВыберите необходимое действие:\n"
            "==============================\n"
            "1. Отобразить весь справочник.\n"
            "2. Найти абонента по имени или фамилии.\n"
            "3. Найти абонента по номеру телефона.\n"
            "4. Добавить абонента в справочник.\n"
            "5. Редактировать данные абонента в справочнике.\n"
            "6. Удалить абонента из справочника.\n"
            "0. Выход из программы.\n")
    choice = int(input("Выбор действия: "))
    return choice


def print_phonebook(filename):  #при выборе пункта 1
    with open(filename, 'r', encoding='utf-8') as file:
        print("\nВ телефонной книге записаны:")
        for line in file:
            contact = line.strip().split(',')
            print(f"{contact[0]} {contact[1]} - {contact[2]}")


def seach_by_FIO(filename): #при выборе пункта 2
    f_name = input("\nВведите фамилию или имя абонента для поиска: ")
    found_contacts = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            contact = line.strip().split(',')
            if f_name.lower() == contact[0].lower() or f_name.lower() == contact[1].lower():
                found_contacts.append(contact)

        if len(found_contacts) > 0:
            for i in found_contacts:
                print(*i)
        else:
            print("Абонет с такой фамилией или именем в телефонной книге отсутствует.")


def seach_by_number(filename): #при выборе пункта 3
    f_name = input("\nВведите номер телефона абонента для поиска: ")
    found_contacts = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            contact = line.strip().split(',')
            if f_name == contact[2]:
                found_contacts.append(contact)

        if len(found_contacts) > 0:
            for i in found_contacts:
                print(*i)
        else:
            print("Абонет с таким номером в телефонной книге отсутствует.")


def add_contact(filename): #при выборе пункта 4
    last_name = input("Введите фамилию абонента: ")
    first_name = input("Введите имя абонента: ")
    tel_number = input("Введите номер телефона абонента: ")
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"\n{last_name},{first_name},{tel_number}")
    print("______________________________\n"
            "Новый контакт успешно добавлен в справочник!")


def edit_contact(filename): #при выборе пункта 5
    f_name = input("\nВведите фамилию, имя или номер абонента, запись которого необходимо отредактировать: ")
    contacts = []
    edit_lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
        
        for i in range(len(contacts)):
            if f_name.lower() == contacts[i][0].lower() or f_name.lower() == contacts[i][1].lower() or f_name == contacts[i][2]:
                print(f"\nНайден контакт: {contacts[i][0]} {contacts[i][1]} - {contacts[i][2]}")
                print("Начать редактирование?\n"
                        "1. Да.\n"
                        "2. Нет.")
                edit_choice = int(input("\nВыбор действия: "))

                if edit_choice == 1:
                    last_name = input("Введите фамилию абонента: ")
                    first_name = input("Введите имя абонента: ")
                    tel_number = input("Введите номер телефона абонента: ")
                    new_contact = [last_name, first_name, tel_number]
                    contacts[i] = new_contact
                    num_ed_cont = i + 1
                    edit_lines.append(num_ed_cont)
                else:
                    i += 1
 
    with open(filename, 'w', encoding='utf-8') as file: #сохранение в файл
        for i in range(len(contacts)):
            if i != len(contacts)-1:    #условие используется чтобы избежать записи в файл последней пустой строки
                file.write(f"{contacts[i][0]},{contacts[i][1]},{contacts[i][2]}\n")
            else:
                file.write(f"{contacts[i][0]},{contacts[i][1]},{contacts[i][2]}")

    if len(edit_lines) > 0:
        print("______________________________\n"
                "Телефонная книга обновлена. Отредактированны контакты №:", *edit_lines)
    else:
        print("______________________________\n"
                "Телефонная книга обновлена. Контакты не редактировались.")


def del_contact(filename):
    f_name = input("\nВведите фамилию, имя или номер абонента, запись которого необходимо удалить: ")
    contacts = []
    del_lines = []
    choise_for_del = []
    with open(filename, 'r', encoding='utf-8') as file:
        
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
        
        for i in range(len(contacts)):
            if f_name.lower() == contacts[i][0].lower() or f_name.lower() == contacts[i][1].lower() or f_name == contacts[i][2]:
                print(f"\nНайден контакт: {contacts[i][0]} {contacts[i][1]} - {contacts[i][2]}")
                print("Удалить контакт?\n"
                        "1. Да.\n"
                        "2. Нет.")
                edit_choice = int(input("\nВыбор действия: "))

                if edit_choice == 1:
                    del_lines.append(contacts[i])
                    choise_for_del.append(i)
                    contacts.pop(i)
                else:
                    i += 1

        # for i in choise_for_del:
        #     contacts.pop(i)
 
    with open(filename, 'w', encoding='utf-8') as file: #сохранение в файл
        for i in range(len(contacts)):
            if i != len(contacts)-1:    #условие используется чтобы избежать записи в файл последней пустой строки
                file.write(f"{contacts[i][0]},{contacts[i][1]},{contacts[i][2]}\n")
            else:
                file.write(f"{contacts[i][0]},{contacts[i][1]},{contacts[i][2]}")

    if len(del_lines) > 0:
        print("______________________________\n"
                "Телефонная книга обновлена. Удален(ы) контакт(ы) :", *del_lines)
    else:
        print("______________________________\n"
                "Телефонная книга обновлена. Контакты не удалялись.")


choice = program_menu()

while choice != 0:
    if choice == 1:
        print_phonebook(phone_book)
        choice = program_menu()
    elif choice == 2:
        seach_by_FIO(phone_book)
        choice = program_menu()
    elif choice == 3:
        seach_by_number(phone_book)
        choice = program_menu()
    elif choice == 4:
        add_contact(phone_book)
        choice = program_menu()
    elif choice == 5:
        edit_contact(phone_book)
        choice = program_menu()
    elif choice == 6:
        del_contact(phone_book)
        choice = program_menu()
    else:
        print("\nВведено некорректное значение! Сделайте выбор в соответствии с пунктами меню.")
        choice = program_menu()
