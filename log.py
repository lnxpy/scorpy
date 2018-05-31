from clr import colors
from datetime import datetime as time

def _save(_stat):
    file = open('logs.txt','a')
    file.write(_stat+' at '+str(time.now())+'\n')
    print(colors.red+'>>'+colors.end+' logs'+colors.red+' wrote'+colors.end+'!')
