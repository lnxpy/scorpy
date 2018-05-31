
from log import _save
from clr import colors
from datetime import datetime as time
from process import _tence
from time import sleep as slp

def _getper():
    print(colors.blue+'>>'+colors.end+' First , for working with scorpy you have to '+colors.blue+colors.bold+'get the superuser permission'+colors.end+'!')
    _start()
def _basename(_path):
    _base = ''
    for i in _path[::-1]:
        if i == '/':
            break
        else:
            _base += i
    _base = (list(_base))
    _base.reverse()
    _base = ''.join(_base)
    return _base

def _start():
    ft = input(colors.blue+'>>'+colors.end+' Enter the text file Path sample '+colors.blue+'(/test.txt)'+colors.end+' ~> ')
    try:
        op = open(ft,'r')
        _save(ft+' Opened')
        print(colors.red+'>> '+colors.end+_basename(ft)+colors.red+' Opened!'+colors.end+'!')
        slp(2)
        _tence((op.read()).lower(),ft)
        op.close()
    except FileNotFoundError:
        _save(ft+' didn\'t Open')
        print(colors.fail+'>>'+colors.end+' File not '+colors.fail+'exist'+colors.end+'!')
        _start()
if __name__ == '__main__':
    _getper()
