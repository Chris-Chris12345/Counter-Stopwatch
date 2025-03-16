from tkinter import *
import time
from tkinter import messagebox

window = Tk()
window.title("Counter Stopwatch")
window.geometry("300x250")

hour = StringVar()
minute = StringVar()
second =  StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hour_entry = Entry(window,width=3,font=("Arial",16,""),textvariable=hour)
minute_entry = Entry(window,width=3,font=("Arial",16,""),textvariable=minute)
second_entry = Entry(window,width=3,font=("Arial",16,""),textvariable=second)

hour_entry.place(x=90,y=50)
minute_entry.place(x=140,y=50)
second_entry.place(x=190,y=50)

def submit():
    try:
        #the input provided by the user is stored in here: temp
        temp = int(hour.get())*3600+int(minute.get())*60+int(second.get())
    except:
        print("Please input the right values.")
        
    while temp >=0:
        #divmod(firstvalue = temp//60,secondvalue = temp%60)
        minute,second = divmod(temp,60)
        #converting the input entered by the user in minutes or seconds to hours
        hour = 00
        if minute > 60:
            hour,minute = divmod(minute,60)

        #using format() method to store the value
        #rounding to 2 decimal places
        hour.set("{00:2d}".format(hour))
        minute.set("{00:2d}".format(minute))
        second.set("{00:2d}".format(second))

        #updating the GUI window after decrementing the temp value every time
        window.update()
        time.sleep(1)
        temp = temp - 1


        if (temp == 0):
            messagebox.showinfo("Timer Finished","Time's up!")

btn = Button(window,text="Set Time Countdown",border="5",command=submit)
btn.place(x=90,y=150)
window.mainloop()