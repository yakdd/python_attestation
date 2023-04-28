import initialization
import view
import import_modul
import export_modul
import change_modul


def start():
    initialization.new_notebook()
    while True:
        action = view.select_action()
        if action == '0':
            break
        elif action == '1':
            export_modul.output_notes()
        elif action == '2':
            import_modul.add_note()
        elif action == '3':
            change_modul.delete_note()
        elif action == '4':
            change_modul.edit_note()
        elif action == '5':
            export_modul.show_note()
        elif action == '6':
            export_modul.filter_notes()

        else:
            export_modul.error()
