import tkinter as tk
from tkinter import *

def encrypter():
    wn = tk.Tk()
    wn.title('EncrPY')
    wn.geometry("1200x600")
    wn.configure(bg='black')

window = tk.Tk()
window.geometry("700x400")
#Terms of Service
window.title("Terms of Service")
ToS_text = tk.Text(window, height=600, width=500)
ToS_text.insert(tk.END, "Terms of Service")
ToS_text.place(relx=.4, rely=.5, anchor="c")
ToS_text.configure(bg='white', fg='black', font=('Calibri', 15))

#Accept
ToS_v2 = tk.Button(window, text='I agree', width=25, command=lambda: [encrypter(), window.destroy], bg="white", fg="black")
ToS_v2.place(bordermode=INSIDE, height=25, width=45)
ToS_v2.place(relx=.43, rely=.9, anchor="c")
#Close
ToS_v2 = tk.Button(window, text='Close', width=25, command=window.destroy, bg="white", fg="black")
ToS_v2.place(bordermode=INSIDE, height=25, width=45)
ToS_v2.place(relx=.5, rely=.9, anchor="c")

#Terms of service'
T = tk.Text(window, height=23, width=60)
T.grid()
T.insert(tk.END, "BY ACCEPTING TO OUR TERMS OF SERVICE, YOU AGREE TO FOLLOW THE FOLLOWING PROHIBITIONS ON OUR LICENSED PRODUCT.")
T.place(relx=.5, rely=.44, anchor="c")
T.configure(bg='white', fg='black', font=('Calibri', 8))


window.mainloop()
