import PySimpleGUI as sg  

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Digite um número: ')],      
          [sg.Input(key='val1')], 
          [sg.Text('Digite outro número: ')],      
          [sg.Input(key='val2')],     
          [sg.Button('Soma'), sg.Button('Subtrai'), sg.Button('Multiplica'), sg.Button('Divide')]]      

window = sg.Window('Soma e subtração', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED:
        break      
    
    if event == 'Soma':
        soma = int(values['val1']) + int(values['val2'])
        sg.popup(f'A soma é {soma}', grab_anywhere=True)
    
    if event == 'Subtrai':
        subtrai = int(values['val1']) - int(values['val2'])
        sg.popup(f'A subtração é {subtrai}', grab_anywhere=True)
        
    if event == 'Multiplica':
        multiplica = int(values['val1']) * int(values['val2'])
        sg.popup(f'A multiplicação é {multiplica}', grab_anywhere=True)
        
    if event == 'Divide':
        divide = int(values['val1']) / int(values['val2'])
        sg.popup(f'A divisão é {divide:.2f}', grab_anywhere=True)
        

window.close()
