import PySimpleGUI as sg

from cleaner.cleaner import prep, clean


layout = [
    [sg.Text('Base directory to clean:'), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Extensions to clean:'), sg.InputText()],
    [sg.Button('Scan'), sg.Button('Cancel')]
]

window = sg.Window('Directory Cleaner', layout)

event, values = window.read()
if event == 'Scan':
    empties = prep(values[0], values[1])
else:
    exit()

window.close()


layout = [
    [sg.Text(f'{len(empties)} empty folders found')],
    [sg.Listbox(values=empties, size=(100, 10))],
    [sg.Text('Delete these folders?')],
    [sg.Button('Yes'), sg.Button('No')]
]

window = sg.Window('Directory Cleaner', layout)

event, values = window.read()

if event == 'Yes':
    clean(empties)

window.close()