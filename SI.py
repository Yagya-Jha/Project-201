from tkinter import *
window = Tk()
window.title("Simple Interest Calculator")
window.geometry("350x600")
window.configure(bg="#e866bd")

def calc():
    principal = float(pricipal.get())
    rate = float(roi.get())
    t = float(time.get())
    i = (principal * rate * t) / 100
    i=float(round(i,2))
    result_label.destroy()
    final_msg=f"Your SI is {i} & Amount is {i+principal}"
    output_msg=Label(result_frame,text=final_msg,fg="black", bg="#e866bd", font=("Calibri",10), bd=2, width=40)
    output_msg.place(x=20,y=40)
    output_msg.pack()

heading = Label(window,text="SI Calculator", fg="black", bg="#e866bd", font=("Calibri",23), bd=6)
heading.place(x=90,y=5)

pricipal_label = Label(window,text="Enter Your Pricipal Amount\n(₹): ", fg="black", bg="#e866bd", font=("Calibri",13), bd=2)
pricipal_label.place(x=2,y=60)
pricipal = Entry(window,text="",bd=2,width=20)
pricipal.place(x=210,y=63)

roi_label = Label(window,text="Enter Your Rate of Interest\n(%/annum): ", fg="black", bg="#e866bd", font=("Calibri",13), bd=2)
roi_label.place(x=2,y=120)
roi = Entry(window,text="",bd=2,width=20)
roi.place(x=210,y=123)

time_label = Label(window,text="How long are you planning\nto keep the money?\n(years) : ", fg="black", bg="#e866bd", font=("Calibri",13), bd=2)
time_label.place(x=2,y=180)
time = Entry(window,text="",bd=2,width=20)
time.place(x=210,y=183)

bttn = Button(window, text="Calculate", bg="#db9437", fg="black", command=calc)
bttn.place(x=130,y=250)

result_frame = LabelFrame(window, text="Result", bg="#e866bd", fg="black")
result_frame.place(x=20,y=400)
result_frame.pack(padx=20,pady=280)

result_label = Label(result_frame, text="", bg="#e866bd",fg="black",font=("Calibri",14), width=30)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()