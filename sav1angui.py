import PySimpleGUI as psg
import os

layout = [
    [psg.Text('Input File:'), psg.FileBrowse(key='-i', enable_events=True)],
    [psg.Text('Output File:'), psg.FileSaveAs(key='-o', enable_events=True)],
    [psg.Text('Encoder:'), psg.Combo(['aom', 'x264', 'x265', 'vp9'], key='-e', readonly=True, enable_events=True)],
    [psg.Text('Workers:'), psg.Slider(range=(1,24), key='-w', orientation='h')],
    [psg.Text('cq-level:'), psg.Slider(range=(0,63), default_value=20, orientation='horizontal', key='-v "--cq-level=')],
    [psg.Text('Cpu-used:'), psg.Slider(range=(0,6), default_value=6, orientation='horizontal', key='--cpu-used="')],
    [psg.OK(), psg.Cancel()]
]

window = psg.Window('Sav1anGUI', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == 'OK':

        #creating the command string
        cmd = 'av1an '
        for key in values:
            cmd += " "
            cmd += key
            tmpvalue = values[key]
            if isinstance(tmpvalue, float) == True:
                tmpvalue = int(tmpvalue)
            cmd += str(tmpvalue)  
            
        #executing the command
        print('Final Command: ', cmd)
        cmd_return = os.system(cmd)
        print(cmd_return)

        break


    if event == psg.WIN_CLOSED or event == 'Cancel':
        break

window.close()


