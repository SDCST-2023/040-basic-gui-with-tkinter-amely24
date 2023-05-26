import tkinter as tk 


window = tk.Tk()
window.title("Example")
window.geometry("260x135")
window.configure(bg="white")

dogphoto=tk.PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2=tk.Label(window, text="Pochacco!", bg="white")
label3=tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg="cyan")

label1.place(x=60, y=0)
label2.place(x=130, y=50)
label3.place(x=0, y=100)

window.mainloop()