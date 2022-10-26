def show_menu():
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')
    choise = int(input('Выберите пункт меню: '))
    return choise
def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)
def input_path():
    path = input('Введите имя файла: ')
    return path
def input_contact():
    name_contact = input('Введите имя: ')
    phone_contact = input('Введите номер: ')
    comment_contact = input('Введите комментарий: ')
    return(name_contact, phone_contact, comment_contact)
def input_change():
    id = int(input('Введите номер контакта: '))
    print('Что изменить?')
    choise = input('0 - имя, 1 - телефон, 2 - комментарий, 3 - отмена: ')
    value = input('Введите изменения: ')
    return(id, choise, value)
def input_remove():
    id = int(input('Введите номер контакта: '))
    return id
def input_search():
    print('Что искать?')
    choise = input('0 - имя, 1 - телефон, 2 - комментарий: ')
    value = input('Введите что искать: ')
    return (choise, value)
def output_search(search_result):
    print('Результаты поиска: ')
    for i in range(0, len(search_result)-1, 2):
        print(search_result[i], *search_result[i+1])







