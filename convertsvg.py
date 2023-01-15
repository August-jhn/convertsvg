import subprocess
import os

target = ''

with open('target.txt', 'r') as f:
    i = 0
    for line in f:
        if i == 0:
            target = line
        i += 1

    f.close()


def count_figures():
    count = 0
    for file in os.listdir(target):
        name, suffix = os.path.splitext(file)
        if "figure" in name and "SVG" in suffix.upper():
            count += 1
    return count

CMDS = [
    'pdflatex to_convert.tex',
    'inkscape -o to_crop.svg to_convert.pdf',
    'inkscape --batch-process --actions="select-all:all;fit-canvas-to-selection;export-filename:{t}figure_{n}.svg;export-do;" to_crop.svg'.format(t= target, n = count_figures())
    
]

DELETESTUFF = [
    'del to_convert.tex',
    'del to_convert.pdf',
    'del to_convert.aux',
    'del to_convert.log',
    'defl to_crop.svg'
]



def run_commands():
    for cmd in CMDS:
        subprocess.run(cmd, shell = True)

def delete_stuff():
    for cmd in DELETESTUFF:
        subprocess.run(cmd, shell = True)

def main():

    delete_stuff()

    print('Welcome to ConvertSvg. This little program does relies on having inkscape and miktex with pdflatex pre-installed.')
    print('\n')
    print('Enter equation to convert:')

    TOCONVERT = ''

    with open('toconvert.txt', 'r') as f:
        for line in f:
            TOCONVERT += line

        f.close()

    TEXT = ''

    with open('format.tex', 'r') as f:
        for line in f:
            
            TEXT += line
            if 'TEXT' in line:
                TEXT += "\n"
                TEXT += TOCONVERT
        f.close()

    with open('to_convert.tex', 'x') as f:
        f.write(TEXT)
        f.close()

    run_commands()
    delete_stuff()
    
if __name__ == "__main__":
    main()