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


def program_menu() -> int:
    print("\nВыберите необходимое действие:\n"
            "==============================\n"
            "1. Открыть телефонный справочник (открыть файл).\n"
            "2. Отобразить весь справочник.\n"
            "3. Найти абонента по имени или фамилии.\n"
            "4. Найти абонента по номеру телефона.\n"
            "5. Добавить абонента в справочник.\n"
            "6. Редактировать данные абонента в справочнике.\n"
            "7. Удалить абонента из справочника.\n"
            "8. Сохранить телефонный справочник в файл.\n"
            "0. Выход из программы.\n")
    choice = int(input("Выбор действия: "))
    return choice


def open_phonebook(filename): #при выборе пункта 1
    contacts = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
    
    return contacts


def print_phonebook(contacts):  #при выборе пункта 2
    print("\nВ телефонной книге записаны:")
    for i in range(len(contacts)):
        print(f"{i + 1}. {contacts[i][0]} {contacts[i][1]} - {contacts[i][2]}")


def seach_by_FIO(contacts): #при выборе пункта 3
    f_name = input("\nВведите фамилию или имя абонента для поиска: ")
    found_contacts = []

    for i in range(len(contacts)):
        if f_name.lower() == contacts[i][0].lower() or f_name.lower() == contacts[i][1].lower():
            found_contacts.append(contacts[i])

    if len(found_contacts) > 0:
        for f_contact in found_contacts:
            print(*f_contact)
    else:
        print("Абонет с такой фамилией или именем в телефонной книге отсутствует.")


def seach_by_number(contacts): #при выборе пункта 4
    f_name = input("\nВведите номер телефона абонента для поиска: ")
    found_contacts = []

    for i in range(len(contacts)):
        if f_name == contacts[i][2]:
            found_contacts.append(contacts[i])

    if len(found_contacts) > 0:
        for f_contact in found_contacts:
            print(*f_contact)
    else:
        print("Абонет с таким номером в телефонной книге отсутствует.")


def add_contact(contacts): #при выборе пункта 5
    last_name = input("Введите фамилию абонента: ")
    first_name = input("Введите имя абонента: ")
    tel_number = input("Введите номер телефона абонента: ")
    new_contact = [last_name,first_name,tel_number]
    contacts.append(new_contact)
    print("______________________________\n"
            "Новый контакт успешно добавлен в справочник!")


def edit_contact(contacts): #при выборе пункта 6
    f_name = input("\nВведите фамилию, имя или номер абонента, запись которого необходимо отредактировать: ")
    edit_lines = []
        
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
    
    if len(edit_lines) > 0:
        print("______________________________\n"
                "Телефонная книга обновлена. Отредактированны контакты №:", *edit_lines)
    else:
        print("______________________________\n"
                "Телефонная книга обновлена. Контакты не редактировались.")


def del_contact(contacts):  #при выборе пункта 6
    f_name = input("\nВведите фамилию, имя или номер абонента, запись которого необходимо удалить: ")
    del_lines = []
    choise_for_del = []

    for i in range(len(contacts)):
        if f_name.lower() == contacts[i][0].lower() or f_name.lower() == contacts[i][1].lower() or f_name == contacts[i][2]:
            print(f"\nНайден контакт: {contacts[i][0]} {contacts[i][1]} - {contacts[i][2]}")
            print("Удалить контакт?\n"
                    "1. Да.\n"
                    "2. Нет.")
            edit_choice = int(input("\nВыбор действия: "))

            if edit_choice == 1: #пока корректно можно удалить только один контакт из книги при одном обращении к функции - сбивается len(contacts)...
                del_lines.append(contacts[i])
                choise_for_del.append(i)
                contacts.pop(i)
            else:
                i += 1
    
    if len(del_lines) > 0:
        print("______________________________\n"
                "Телефонная книга обновлена. Удален(ы) контакт(ы) :", *del_lines)
    else:
        print("______________________________\n"
                "Телефонная книга обновлена. Контакты не удалялись.")


def save_phonebook(filename, contacts): #при выборе пункта 8
    with open(filename, 'w', encoding = 'utf-8') as file:
        for i in range(len(contacts)):
            if i != len(contacts) - 1:    #условие используется чтобы избежать записи в файл последней пустой строки
                file.write(f"{contacts[i][0]},{contacts[i][1]},{contacts[i][2]}\n")
            else:
                file.write(f"{contacts[i][0]},{contacts[i][1]},{contacts[i][2]}")
        
        print("______________________________\n"
                "Телефонная книга сохранена в файл. Запись прошла успешно.")


#путь к файлу указываем явно - на всякий случай. Также можно реализовать функцию выбора директории расположения файла (не хватило времени)
file_path = '/run/media/evgeny/My_storage/01_DATA/Обучение GeekBrains/Work/PYTHON_intro/08_Seminar/phone_book.txt'
choice = program_menu()
contacts = open_phonebook(file_path)

while choice != 0:
    if choice == 1:
        open_phonebook(file_path)
        print("\nДанные из файла считаны.")
        choice = program_menu()
    elif choice == 2:
        print_phonebook(contacts)
        choice = program_menu()
    elif choice == 3:
        seach_by_FIO(contacts)
        choice = program_menu()
    elif choice == 4:
        seach_by_number(contacts)
        choice = program_menu()
    elif choice == 5:
        add_contact(contacts)
        choice = program_menu()
    elif choice == 6:
        edit_contact(contacts)
        choice = program_menu()
    elif choice == 7:
        del_contact(contacts)
        choice = program_menu()
    elif choice == 8:
        save_phonebook(file_path, contacts)
        choice = program_menu()
    else:
        print("\nВведено некорректное значение! Сделайте выбор в соответствии с пунктами меню.")
        choice = program_menu()