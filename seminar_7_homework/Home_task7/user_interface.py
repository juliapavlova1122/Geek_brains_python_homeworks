from input_data import add_contact
from contacts_op import read_contacts, find_contact


def user_interface():
    flag = True
    while flag: 
        print("\n***** Добро пожаловать в телефонный справочник! *****\n\nВыберите пункт меню для продолжения:")
        while True:
            print("1 - Найти контакт")
            print("2 - Добавить контакт")
            print("3 - Показать все контакты")
            print("4 - Выход")
            choice = input()
            if choice not in ["1", "2", "3", "4"]:
                print("!!Выбран неверный пункт меню!!\nПопробуйте ещё раз")
                continue
            if choice == "1": 
                find_contact()
                break
            elif choice == "2":
                add_contact()
                break
            elif choice == "3":
                read_contacts()
            else: 
                flag = False
                break