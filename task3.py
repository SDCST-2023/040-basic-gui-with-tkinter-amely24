import tkinter as tk 


window = tk.Tk()
window.title("Example")
window.geometry("800x250")
window.configure(bg="white")

dogphoto=tk.PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2=tk.Label(window, text="Pochacco!", bg="white")
label3=tk.Label(window, text="A cuddly little puppy! This is from the same creators who brought you Keropi and Kero Kero", bg="cyan")

label1.grid(row=1, column=2)
label2.grid(row=1, column=3)
label3.grid(row=2, column=1, columnspan=4)

window.mainloop()