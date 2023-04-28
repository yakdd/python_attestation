from datetime import datetime


def get_id():
    with open('notebook.csv', 'r', encoding='utf-8') as notes:
        return max([int(note.split(';')[0]) for note in notes.readlines()[1:]])


def add_note():
    new_id = str(get_id() + 1)
    with open('notebook.csv', 'a', encoding='utf-8') as notes:
        title = input('Введите заголовок заметки: ')
        text = input('Введите текст заметки: ')
        text = text.replace(';', '|')
        date = datetime.now().strftime('%d.%m.%Y %H:%M')
        notes.write(f'{new_id};{title};{date};{text}\n')
        print('Заметка сохранена')
