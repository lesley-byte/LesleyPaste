import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [ [sg.Text("Text to paste from hotkeyb.ahk")],
           [sg.Text("Enter text for ctrl-a"), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Lesley Pastey', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print ('you entered', values[0])
    file1 = open(r"C:\Users\phosp\hotkeyb.ahk", "w+")
    L = ["^a:: \n", "Send, "]
    s = values[0]
    s2 = " \n"
    s3 = "return"
    file1.writelines(L)
    file1.write(s)
    file1.write(s2)
    file1.write(s3)

    file1.close()
    file1 = open(r"C:\Users\phosp\hotkeyb.ahk", "r")
    print(file1.read())
    file1.close()
window.close()


