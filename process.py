from clr import colors
from log import _save

def _tence(_text,_name):
    op = open('coded.txt','a')
    for i in _text:
        op.write(chr(ord(i)+1024))
    op.close()
    print(colors.red+'>> '+colors.end+'Decoding '+colors.red+'Completed'+colors.end+'!')
    _save('Decoding '+_name)
    print(colors.red+'>> '+colors.end+'Open the '+colors.under+'coded.txt'+colors.end+'!')
