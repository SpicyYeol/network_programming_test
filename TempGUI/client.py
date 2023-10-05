from tkinter import *

#섭씨 온도를 서버로 전송
def calculate():
    global temp
    temp = float(entry1.get()) #Read a temp
    #entry1.delete(0,END) #입력 창을 지운다
    #sock.send(str(temp).encode()) #send the temp in C to server


root = Tk()
message_label = Label(text='Enter a temperature(C)  ',font=('Verdana', 16))
entry1 = Entry(font=('Verdana', 16), width=5)

recv_label = Label(text='Temperature in F  ',font=('Verdana', 16))
entry2 = Entry(font=('Verdana', 16), width=5)

calc_button = Button(text='전송', font=('Verdana', 12), command=calculate)

message_label.grid(row=0, column=0, sticky=W)
recv_label.grid(row=1, column=0, sticky=W)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
calc_button.grid(row=0, column=2, padx=10, pady=10)


root.mainloop()