from csv_creator import creat_csv
from os.path import exists


def write_contact(sn, n, mn, p_num, e, descr):
    with open(FILE_NAME, "a", encoding="UTF-8") as f:
        f.write(f"{sn}, {n}, {mn}, {p_num}, {e}, {descr};\n")


def read_contacts():
    with open(FILE_NAME, "r", encoding="UTF-8") as f: 
        print(f.read())


def find_contact():
    sn = input("Введите фамилию контакта: ")
    with open(FILE_NAME, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            if line.startswith(sn):
                print("Найдено:\n", line)

                
FILE_NAME = "phonebook.csv"
valid = exists(FILE_NAME)
if not valid:
    creat_csv() 
