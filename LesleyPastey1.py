import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [ [sg.Text("Letter to paste to"), sg.InputText()],
           [sg.Text("Enter text for letter"), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Lesley Pastey', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print ('you entered', values[1])
    file1 = open(r"C:\Users\phosp\hotkeyb.ahk", "w+")
    L0 = ["^"]
    L1 = values[0]
    L2 = [":: \n", "Send, "]
    s = values[1]
    s2 = " \n"
    s3 = "return"
    file1.writelines(L0)
    file1.writelines(L1)
    file1.writelines(L2)
    file1.write(s)
    file1.write(s2)
    file1.write(s3)

    file1.close()
    file1 = open(r"C:\Users\phosp\hotkeyb.ahk", "r")
    print(file1.read())
    file1.close()
window.close()
