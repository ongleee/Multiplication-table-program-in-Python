import tkinter as tk
def show_output():
    number = int(number_input.get())
    if number == 0:
        output_label.configure(text='ศูนย์พ่อมึงอะ')
        return
    output = ''
    for i in range(1,13):
        output += str(number) + ' X ' + str(i) + ' = ' + str(number * i) + '\n'
    output_label.configure(text=output)

window = tk.Tk()
window.title("HENRY")
window.minsize(width=400,height=400)

title_label = tk.Label(master=window,text="สูตรคูณแม่")
title_label.pack(pady=20)

number_input = tk.Entry(master=window,width=20,)
number_input.pack()
number_input.config(font=("Arial", 12))

go_button = tk.Button(master=window, text="ได้แก่",command=show_output,width=25,height=1)
go_button.pack(pady=10)

output_label = tk.Label(master=window)
output_label.pack(pady=20)


window.mainloop()