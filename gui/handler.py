from tkinter import *
root = Tk()
# root.geometry("700x400+200+200")
import time

def moveWindow():
	global count
	if count == 1000:
		count = 0
	else:
		count +=1
		
	root.geometry("700x400+200"+str(count)+"+200")
	time.sleep(0.1)
	root.after(1, moveWindow)
	

def buttonSubmit_click():
	print("I am clicked") # these would be logged in the terminal


def helloSubmit_click():
	print("Hello Button is clicked") # this would be logged in the terminal

# root.geometry("300x300")
btnSubmit = Button(master=root, text="Submit", command=buttonSubmit_click)
btnHello = Button(master=root, text="Hello", command=helloSubmit_click)
count = 0
btnSubmit.pack()
btnHello.pack()



moveWindow()
root.mainloop()