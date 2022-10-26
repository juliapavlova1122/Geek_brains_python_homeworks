def creat_csv():
    FILE_NAME = "phonebook.csv"
    with open (FILE_NAME, "w", encoding = 'UTF-8') as f:
        f.write(f"Фамилия, Имя, Отчество, Номер телефона, E-mail, Описание\n")
        