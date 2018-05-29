'''
By trial and error you may find out how many waits are necessary for the script to work
Use IDLE3 to copy the printed code.
'''

def jb(fps, waits):
    i = 2
    script = 'alias jb1 "fps_max ' + str(fps) + ';w;+jump;w;-jump;alias @jb jb2;bxt_append _jb"\n'
    for waits in range(0, waits):
        script += 'alias jb' + str(i) + ' "w;alias @jb jb' + str(i+1) + ';bxt_append _jb"\n'
        i += 1

    script += 'alias jb' + str(i) + ' "+duck;w 5;say jumpbug!;-duck;+jump;w;-jump;alias @jb"\n\n'
    script += 'alias +jumpbug "alias _jb @jb;jb1"\n'
    script += 'alias -jumpbug "alias _jb;fps_max 100"'
    print(script)

jb(34.48276, 98)
