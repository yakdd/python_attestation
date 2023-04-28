import constants


def new_notebook():
    try:
        with open('notebook.csv', 'r', encoding='utf-8') as notes:
            pass
    except FileNotFoundError:
        with open('notebook.csv', 'w', encoding='utf-8') as notes:
            notes.write(constants.header)
