import time
from tkinter import *
seconds =0
minutes =0
hours =0
stop =0
def start():
   global seconds,minutes,hours
   time.sleep(1)
   seconds = seconds+1
   if (seconds ==60) :
      seconds =0
      minutes+=1
   if (minutes ==60) :
      minutes =0
      hours +=1
   if (stop==0) :
      label =Label(mw, text=str(hours)+":"+str(minutes)+":"+str(seconds))
      #foreground ='red',bg="black",width=10
      label.after(300,start)
      label.place(x = 50,y = 100)
def stopwatch():
	global stop
	stop=1
mw = Tk()
mw.title("STOPWATCH")
mw.geometry("210x160")
mw.configure(bg="black")
startbutton= Button(mw,text="Start",command=start).place(x=20,y=20)
stopbutton = Button(mw,text="Stop",command=stopwatch).place(x=100,y=20)
mw.mainloop()
