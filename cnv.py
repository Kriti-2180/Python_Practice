from tkinter import *

def mouse_down(evt):
        global px,py
        px = evt.x 
        py = evt.y
    
def mouse_move(evt):
        global px,py
        cnv.create_line(px,py,evt.x,evt.y)
        px = evt.x		 		
        py = evt.y 

win=Tk()
cnv=Canvas(win,width=600,height=300,bg='white')
cnv.pack(padx=20,pady=20)

cnv.bind('<Button-1>',mouse_down)
cnv.bind('<B1-Motion>',mouse_move)

mainloop()
