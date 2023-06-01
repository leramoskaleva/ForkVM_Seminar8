def greetings():
    print(
        'Привет хозяин'
    )
    return greetings


def menu():
    print(
        '1 – Показать все контакты\n'
        '2 – Добавить контакт\n'
        '3 – Поиск\n'
        '4 – Изменить контакт\n'
        '5 - Удалить контакт\n'
        '6 – Выход'
    )


def error():
    print(
        'Error. Повторите ввод'
    )


def show_contacts(date: list):
    return None


def success(res):
    return None


def not_success(res):
    return None

def change_phone_number(contact):
   return None

def delete_contact(contact):
   return None



if __name__ == '__main__':
    menu()
