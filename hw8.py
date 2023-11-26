'''
Задание, для урока 8. Работа с файлами.

Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
'''

import os

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                contact_data = line.strip().split(', ')
                contacts.append({
                    'last_name': contact_data[0],
                    'first_name': contact_data[1],
                    'middle_name': contact_data[2],
                    'phone_number': contact_data[3]
                })
    return contacts

def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}\n")

def print_contacts(contacts):
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['last_name']} {contact['first_name']} {contact['middle_name']} - {contact['phone_number']}")
def search_contacts(contacts, key, value):
    result = [contact for contact in contacts if value.lower() in contact[key].lower()]
    return result

def copy_contact(contacts, from_index, to_filename):
    if 1 <= from_index <= len(contacts):
        contact_to_copy = contacts[from_index - 1]
        with open(to_filename, 'a') as file:
            file.write(f"{contact_to_copy['last_name']}, {contact_to_copy['first_name']}, {contact_to_copy['middle_name']}, {contact_to_copy['phone_number']}\n")
        print("Контакт успешно скопирован.")
    else:
        print("Некорректный номер строки.")

def edit_contact(contacts, index_to_edit):
    if 1 <= index_to_edit <= len(contacts):
        contact_to_edit = contacts[index_to_edit - 1]
        print(f"Текущие данные контакта: {contact_to_edit}")
        contact_to_edit['last_name'] = input("Введите новую фамилию: ")
        contact_to_edit['first_name'] = input("Введите новое имя: ")
        contact_to_edit['middle_name'] = input("Введите новое отчество: ")
        contact_to_edit['phone_number'] = input("Введите новый номер телефона: ")
        print("Контакт успешно изменен.")
    else:
        print("Некорректный номер строки.")

def delete_contact(contacts, index_to_delete):
    if 1 <= index_to_delete <= len(contacts):
        del contacts[index_to_delete - 1]
        print("Контакт успешно удален.")
    else:
        print("Некорректный номер строки.")

def main():
    source_filename = 'contacts.txt'
    destination_filename = 'copied_contacts.txt'
    
    contacts = load_contacts(source_filename)
    
    while True:
        print("\n1. Вывести контакты")
        print("2. Добавить контакт")
        print("3. Сохранить контакты")
        print("4. Поиск контакта")
        print("5. Копировать контакт")
        print("6. Изменить контакт")
        print("7. Удалить контакт")
        print("8. Выход")
        
        choice = input("Выберите действие (1-8): ")
        
        if choice == '1':
            print_contacts(contacts)
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            
            contacts.append({
                'last_name': last_name,
                'first_name': first_name,
                'middle_name': middle_name,
                'phone_number': phone_number
            })
        elif choice == '3':
            save_contacts(contacts, source_filename)
            print("Контакты сохранены в файле.")
        elif choice == '4':
            search_key = input("Выберите характеристику для поиска (last_name, first_name, middle_name, phone_number): ")
            search_value = input("Введите значение для поиска: ")
            result = search_contacts(contacts, search_key, search_value)
            if result:
                print("Результаты поиска:")
                print_contacts(result)
            else:
                print("Ничего не найдено.")
        elif choice == '5':
            index_to_copy = int(input("Введите номер строки для копирования: "))
            copy_contact(contacts, index_to_copy, destination_filename)
        elif choice == '6':
            index_to_edit = int(input("Введите номер строки для изменения: "))
            edit_contact(contacts, index_to_edit)
        elif choice == '7':
            index_to_delete = int(input("Введите номер строки для удаления: "))
            delete_contact(contacts, index_to_delete)
        elif choice == '8':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
