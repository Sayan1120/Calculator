import PySimpleGUI as sg

def createWindow(theme):
    

    sg.theme('BlueMono')
    sg.set_options(font = 'Franklin 15', button_element_size= (6, 3))
    button_size = (6, 3)
    padding = (10, 25)
    layout = [
        [sg.Text('', 
                 font='Franklin 27', 
                 justification='right', 
                 expand_x = True, 
                 pad = padding,
                 right_click_menu= themeMenu, key='-TEXT-')], 
        [sg.Button('Clear', expand_x = True), sg.Button('Enter', expand_x = True)], 
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('/', size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)]
    ]
    return sg.Window('Calculator', layout)

themeMenu = ['menu', ['LightGrey1', 'dark', 'DarkGrey8', 'random']]

window = createWindow('BlueMono')

current_number = []
full_op = []

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event in themeMenu[1]:
        window.close()
        window = createWindow(event)
        
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_number.append(event)
        num_string = ''.join(current_number)
        window['-TEXT-'].update(num_string)
    
    if event in ['*', "/", '+', '-']:
        full_op.append(''.join(current_number))
        current_number = []
        full_op.append(event)
        window['-TEXT-'].update('')
        
    if event == 'Enter':
        full_op.append(''.join(current_number))
        result = eval(''.join(full_op))
        window['-TEXT-'].update(result)
        full_op = []

    if event == 'Clear':
        current_number = []
        full_op = []
        window['-TEXT-'].update('')
  
        
window.close()
