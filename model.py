import view
textfile = open("file.txt", "w+")

def data():
    with open('file.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')[:-1]
        
    return data


def add_contact(contact):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        file.write('\n')
        return contact


def find_contact(data):
  with open('file.txt', 'a', encoding='utf-8') as file:
     command = int(input('Введите данные контакта для поиска: ')) # view.py
     if command == 1:
           find_name = input('Введите ФИО: ')
           for command in data:
              if data[command] == find_name:
                  print(data[command])

     elif command == 2:
       find_phone = input('Введите номер телефона: ')
       for command in data:
           if data[command] == find_phone:
               print(data[command])
     else: 
        print('Ошибка ввода')


def change_phone_number(contact):
  with open("file.txt", "r+") as file:
    value = file.read()
    if contact in value:
      new_contact = input('Введите изменения:')
      value = value.replace( contact, new_contact)
      with open("file.txt", "w") as file2:
         file2.write(value)
      view.success()
    else:
      view.not_success()
  


def delete_contact(contact):
   return None