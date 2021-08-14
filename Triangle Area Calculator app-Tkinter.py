from tkinter import *
window =Tk()
window.title("Triangle Area Calculator App")
window.geometry('500x300')
label1= Label(window,text='Enter the Height of Triangle',fg='blue',font=('Arial',14))
label1.grid(row=0,column=0,padx=5,pady=10)
label2= Label(window,text='Enter the Base  of Triangle',fg='blue',font=('Arial',14))
label2.grid(row=1,column=0,padx=5,pady=10)

height= IntVar()
blenth =IntVar()
textbox1= Entry(window,textvariable=height,fg='blue',font=('Arial',14))
textbox1.grid(row=0,column=1)
textbox2= Entry(window,textvariable=blenth,fg='blue',font=('Arial',14))
textbox2.grid(row=1,column=1)
def findArea():
    area=0.5*height.get()*blenth.get()
    emptylabel.config(text='The Area is:'+str(area))

button1 = Button(window,command=findArea,text='Find Area',fg='blue',font=('Arial',14))
button1.grid(row=2,column=1,sticky=W)
emptylabel=Label(window,fg='green',font=('Arial',14))
emptylabel.grid(row=3,column=1,sticky=W,pady=20)

window.mainloop()
