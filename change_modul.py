import constants
from datetime import datetime
import export_modul


def check_id():
    id = input('>>> ')
    with open('notebook.csv', 'r', encoding='utf-8') as file:
        id_list = [line.split(';')[0] for line in file][1:]
    if id in id_list:
        return id
    return False


def delete_note():
    export_modul.output_notes()
    print('Выберете ID заметки для удаления: ')
    del_id = check_id()
    if del_id:
        with open('notebook.csv', 'r+', encoding='utf-8') as notes:
            notes_without_head = notes.readlines()[1:]
            notes.seek(0)
            notes.write(constants.header)
            for note in notes_without_head:
                if del_id != note.split(';')[0]:
                    notes.write(note)
            notes.truncate()
        print('Заметка удалена')
    else:
        export_modul.error()


def edit_note():
    export_modul.output_notes()
    print('Выберете ID заметки для редактирования: ')
    edit_id = check_id()
    if edit_id:
        while True:
            print('Выберете действие:')
            print('  1 - редактировать заголовок')
            print('  2 - редактировать текст заметки')
            change_action = input('>>> ')
            if change_action in ['1', '2']:

                with open('notebook.csv', 'r+', encoding='utf-8') as notes:
                    notes_without_head = notes.readlines()[1:]
                    notes.seek(0)
                    notes.write(constants.header)
                    for note in notes_without_head:
                        if edit_id == note.split(';')[0]:
                            note = note.rstrip('\n\r')
                            if change_action == '1':
                                title = input('Введите новый заголовок: ')
                                text = note.split(';')[3]
                            elif change_action == '2':
                                new_text = input('Введите новый текст: ')
                                text = new_text.replace(';', '|')
                                title = note.split(';')[1]
                            date = datetime.now().strftime('%d.%m.%Y %H:%M')
                            notes.write(f'{edit_id};{title};{date};{text}\n')
                        else:
                            notes.write(note)
                    notes.truncate()
                print('Заметка отредактирована')

                return
            export_modul.error()
    else:
        export_modul.error()
