#!/usr/bin/env python3
import tkinter
from time import strftime

# outputs in a box the current time format
def tic():
    rel['text'] = strftime('%H:%M:%S')

def tac():
    tic()
    rel.after(1000, tac) # calls again 'tic' function after 1 sec

rel = tkinter.Label()
rel['font'] = 'Helvetica 120 bold'
rel.pack()
tac()
# para que funcione como um script, temos que chamar mainloop,
# senão o programa termina imediatamente após a chamada tac()
rel.mainloop()