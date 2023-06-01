def greetings():
    print('Приветствую тебя, хозяин!')


def menu():
    print(
        '1 – Показать все контакты\n'
        '2 – Добавить контакт\n'
        '3 – Поиск\n'
        '4 – Изменить контакт\n'
        '5 - Удалить контакт\n'
        '6 – Выход'
    )

def success(res):
    print('Успешно')

def not_success(res):
    print('Не успешно')

def show_contacts(data):
    return data
    
def error():
    print('Ошибка. Повторите ввод')

 

if __name__ == '__main__':
    menu()
