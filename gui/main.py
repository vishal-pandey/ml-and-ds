import tkinter
import time
root = tkinter.Tk()


root.geometry("700x400+200+200")

# 200+200 defines where to position the window on the desktop

# Defining the title of the window
root.title("Vishal Pandey")

# Setting the max and min of the window
root.minsize(200, 200) # minimum size of the window 
root.maxsize(800, 800) # maximum size of the window
 

# Defining the buttons
btn1 = tkinter.Button(master=root, text="Button 1", width=15, height=3, bg='red', fg="red",  font=("Times New Roman", 16), bd=1000) # 15 and 3 are characters
btn2 = tkinter.Button(master=root, text="Button 2")
btn3 = tkinter.Button(master=root, text="Button 3")
btn4 = tkinter.Button(master=root, text="Button 4")
btn5 = tkinter.Button(master=root, text="Vishal Pandey")

# setting button parameters with dictionary arguments
btn1['fg']= 'green'


btn2.config(fg="green", width=15, height=3,  font=('Times New Roman', 16))
btn3.config(fg="green", width=15, height=3,  font=('Times New Roman', 16))
btn4.config(fg="green", width=15, height=3,  font=('Times New Roman', 16))
btn5.config(fg="green", width=15, height=3,  font=('Times New Roman', 16))


# positioning the button on the window created
btn1.pack(side='left')
btn2.pack(side='right')
btn3.pack()
btn4.pack(side='bottom')
btn5.place(x=300, y=150)

# btn1.pack(side='left')
# btn1.place(x=500, y=500)
# btn1.grid(row=0, column=1)
# btn2.grid(row=0, column=2)
# btn3.grid(row=0, column=3)





# Main loop creates the window on the desktop without this the window would not be created
root.mainloop()
for i in range(100):
	root.geometry("700x400+200"+str(i)+"+200")
	# time.sleep(0.5)
