from contacts_op import write_contact


def add_contact():
    print("Заполните данные нового контакта:")
    flag = True
    while flag:
        surname = input("Фамилия: ")
        name = input("Имя: ")
        midname = input("Отчество: ")
        phone_num = input("Телефонный номер (например, +7...): ")
        eml = input("E-mail: ")
        description = input("Описание: ")
        confirm = input("\nНаберите 1 для сохранения контакта или нажмите любую квавишу для возврата в меню: ")
        if confirm == "1":
            write_contact(surname, name, midname, phone_num, eml, description)
        else: 
            flag = False
