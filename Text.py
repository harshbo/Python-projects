from tkinter import *
def submit():
	input = text.get("1.0" ,END)
	print(input)
window = Tk()
text = Text(window,bg="light yellow",font =("Ink Free",20),height=10,width=20,fg = "brown")
text.pack()
button = Button(window,text="submit",command=submit,cursor ="trek")
button.pack()
window.mainloop()
