import constants


def columns_width(notes):
    id_column_width = max([len(note.split(';')[0]) for note in notes]) + constants.empty_space
    title_column_width = max([len(note.split(';')[1]) for note in notes]) + constants.empty_space
    date_column_width = max([len(note.split(';')[2]) for note in notes]) + constants.empty_space
    text_column_width = max([len(note.split(';')[3][:constants.note_length + 3]) for note in notes])
    width_list = [id_column_width, title_column_width, date_column_width, text_column_width]
    return width_list


def output_notes():
    with open('notebook.csv', 'r', encoding='utf-8') as notes:
        notes_list = [note for note in notes]
        width_list = columns_width(notes_list)
        table_width = sum(width_list)

        notes.seek(0)
        print('-' * table_width)
        head = notes.readline().rstrip().split(';')
        for indx, column in enumerate(head):
            width = width_list[indx]
            print('{0: <{1}}'.format(column, width), end='')
        print()
        print('-' * table_width)

        notes.seek(0)
        for indx, line in enumerate(notes):
            if indx < 1:
                continue
            else:
                elements = line.rstrip().split(';')
                for i, elem in enumerate(elements):
                    width = width_list[i]
                    elem = elem.replace('|', ';')
                    if i == 3:
                        if len(elem) > 10:
                            print('{0: <{1}}'.format(elem[:constants.note_length] + '...', width), end='')
                        else:
                            print('{0: <{1}}'.format(elem, width), end='')
                    else:
                        print('{0: <{1}}'.format(elem, width), end='')
                print()
        print('-' * table_width)


def show_note():
    search = input('Выберете ID или заголовок заметки: ')
    with open('notebook.csv', 'r', encoding='utf-8') as notes:
        not_found = True
        for note in notes:
            note_elements = note.rstrip().split(';')
            if (search == note_elements[0]) or (search == note_elements[1]):
                not_found = False
                print_find_notes(note)
        if not_found:
            error()


def filter_notes():
    find_date = input('Введите дату для поиска в формате "dd.mm" или "mm.yyyy": ')
    with open('notebook.csv', 'r', encoding='utf-8') as notes:
        not_found = True
        for note in notes:
            note_date = note.split(';')[2]
            if len(find_date) == 5 and find_date == note_date[:5]:
                not_found = False
                print_find_notes(note)
            elif len(find_date) == 7 and find_date == note_date[3:10]:
                not_found = False
                print_find_notes(note)
        if not_found:
            print('Заметок не найдено')


def print_find_notes(note):
    note = note.rstrip().split(';')
    for i, elem in enumerate(note):
        if i == 3:
            print(f'{elem.rstrip()}', end='\n')
        else:
            print(f'{elem.rstrip()}', end='\t')


def error():
    print('Ошибка ввода. Попробуйте еще раз!')
