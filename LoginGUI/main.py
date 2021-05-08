from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter import messagebox

u_name = 'k'
u_pass = 'k'
success_msg = 'Login Successfully!'
fail_msg = 'Wrong Password!'


def quit_window():
    confirmation = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                          icon='warning')
    if confirmation == 'yes':
        window.quit()
    else:
        pass


def login_success():
    success_name = user_entry.get()
    success_pass = pass_entry.get()
    if success_pass == u_pass and success_name == u_name:
        user_name1 = ttk.Label(window, text=success_msg, font=('Google Sans', 12, 'normal'))
        user_name1.grid(row=4, column=0, columnspan=2)
    else:
        user_name1 = ttk.Label(window, text=fail_msg, font=('Google Sans', 12, 'normal'))
        user_name1.grid(row=4, column=0, columnspan=2)


def about():
    messagebox.showinfo('About Us', 'This login page was designed with love by Keneli Tech')


window = Tk()
window.title('Login Form')
window.geometry('300x400+550+200')
icon = PhotoImage(file='img/login.png')
window.iconphoto(False, icon)
window.resizable(False, False)
style = ThemedStyle(window)
style.set_theme("breeze")
s = ttk.Style()
s.configure('my.TButton', font=('Google Sans', 14, 'bold'))

# Create Menu Bar
menuBar = Menu(window, background='lightblue', foreground='black',
               activebackground='#004c99', activeforeground='white')
window.config(menu=menuBar)
# File Menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Sign Up")
fileMenu.add_command(label="Login")
fileMenu.add_separator()
fileMenu.add_command(label="Settings")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit_window)
menuBar.add_cascade(label="File", menu=fileMenu)
# Help Menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=about)
helpMenu.add_command(label="How to ->")
menuBar.add_cascade(label="Help", menu=helpMenu)

top_label_img = PhotoImage(file='img/password.png')
top_label = Label(window,
                  image=top_label_img
                  )
top_label.grid(row=0, column=0, columnspan=2, pady=25)

user_name = ttk.Label(window, text='Username', font=('Google Sans', 14, 'bold'))
user_name.grid(row=1, column=0, padx=5)
user_entry = ttk.Entry(window, font=('Google Sans', 14, 'normal'), width=14)
user_entry.grid(row=1, column=1, padx=5, pady=12)

user_pass = ttk.Label(window, text='Password', font=('Google Sans', 14, 'bold'))
user_pass.grid(row=2, column=0, padx=5)
pass_entry = ttk.Entry(window, font=('Google Sans', 14, 'normal'), width=14, show='*')
pass_entry.grid(row=2, column=1, padx=5)

submit_btn = ttk.Button(window, text='Login', width=12, style='my.TButton', command=login_success)
submit_btn.grid(row=3, column=1, columnspan=2, pady=10)

# Calling Main()
window.mainloop()
