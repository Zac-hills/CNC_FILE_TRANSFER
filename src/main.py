import PySimpleGUI as sg
import serial.tools.list_ports
import os

comlist = [port.device for port in serial.tools.list_ports.comports()]

selected_com_port = ''
button_id = 'BUTTON-ID'
combo_id = 'LIST-ID'
layout = sg.theme("DarkTeal2")
layout = [[sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse()], [sg.Listbox(list(comlist), size=(20,4), enable_events=True, key=combo_id)], [sg.Button('Transfer file', key=button_id)]]

# Create the window
window = sg.Window("CNC FILE TRANSFER", layout)


def transfer_file(file_name):
    command = f"COPY \"{file_name.replace(os.sep, '/')}\" /B {selected_com_port} /B"
    print(command)
    os.system(f'cmd /c "{command}"')
    return

# Create an event loop
while True:
    event, values = window.read()

    if event != None:
        print(event)
    print(values)
    if len(values[combo_id]):
        selected_com_port = values[combo_id][0]
    if event == button_id and selected_com_port != '' and values['Browse'] != None:
            transfer_file(values['Browse'])
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()