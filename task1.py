import tkinter as tk 


window = tk.Tk()
window.title("tk")
window.geometry("600x50")
entry1=tk.Entry(window, width=20)
label1=tk.Label(window, text="x")
entry2=tk.Entry(window, width=20)
entry3=tk.Entry(window, width=20)
button=tk.Button(window, text="=")
entry1.grid(row=1, column=1)
label1.grid(row=1, column=2)
entry2.grid(row=1, column=3)
button.grid(row=1, column=4)
entry3.grid(row=1, column=5, columnspan=2)
window.mainloop()