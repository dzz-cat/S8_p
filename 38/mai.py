# # Дополнить телефонный справочник возможностью изменения и удаления данных. 
# # Пользователь также может ввести имя или фамилию, 
# # и Вы должны реализовать функционал для изменения и удаления данных


phonebook = {
    "Иванов": "123456789",
    "Петров": "987654321",
    "Сидоров": "555555555"
}

def add_contact(name, phone_number):
    phonebook[name] = phone_number

def update_contact(name, phone_number):
    if name in phonebook:
        phonebook[name] = phone_number
    else:
        print("Контакт не найден")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
    else:
        print("Контакт не найден")

def search_contact(name):
    if name in phonebook:
        print("Контакт найден:")
        print("Имя:", name)
        print("Телефон:", phonebook[name])
    else:
        print("Контакт не найден")

def change_contact(name):
    if name in phonebook:
        print("Выберите действие:")
        print("1. Изменить имя")
        print("2. Изменить телефон")
        choice = int(input("Введите номер действия: "))
        
        if choice == 1:
            new_name = input("Введите новое имя: ")
            phone_number = phonebook[name]
            delete_contact(name)
            add_contact(new_name, phone_number)
            print("Контакт успешно изменен")
            
        elif choice == 2:
            new_phone_number = input("Введите новый телефон: ")
            update_contact(name, new_phone_number)
            print("Контакт успешно изменен")
            
        else:
            print("Некорректный выбор")
    else:
        print("Контакт не найден")

def remove_contact(name):
    if name in phonebook:
        delete_contact(name)
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")


