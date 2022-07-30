from cProfile import label
from curses import window
from tkinter import *
from typing_extensions import Self
from PIL import ImageTk, Image # pip install pillow

class LoginForm: 
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        
# this definition makes a big window that creats the offical logiin page ==== 


# ============= background image =================
Self.bg_frame = Image.open('image\\2314983.jpeg')
photo = ImageTk.PhotoImage(Self.bg_frame)
Self.bg_panel = Label(Self,window, image=photo)
Self.bg_panel.image = photo
Self.bg_panel.pack(fill='both', expand='yes') 

# ================ login frame ===================
Self.lgn_frame = Frame(Self.window, bg='#040405', width='950', height=600)
Self.lgn_frame.place(x=200, y=70)

Self.txt = 'WELCOME' 
Self.heading = Label(Self.lgn_frame, text=Self.text, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
Self.heading.place(x=80, y=30, width=300, height=30)

# ========== left side image ====================
Self.side_image = Image.open('images\\simple cloud.webp')
photo = PhotoImage(Self.side_image)
Self.side_image_label = Label(Self,window, image=photo, bg='#040405')
Self.side_image_label = photo
Self.side_image_label.pack(x=5, y=100)

# ============== sign in image ==================
Self.sign_in_image = Image.open('images\\39a1eb1485516800d84981a72840d60e.jpeg')
photo = PhotoImage(Self.side_image)
Self.sign_in_image_label = Label(Self,window, image=photo, bg='#040405')
Self.sign_in_image_label = photo
Self.sign_in_image_label.pack(x=620, y=130)

Self.sign_in_label = Label(Self.lgn_frame, text='Sign In', bg='#040405', fg='white', 
font=('yu gothic ui', 13, 'bold'))

Self.sign_in_label.place(x=650, y=240)

# ================ Username ===============
Self.username_label = Label(Self.lgn_frame, text='Username', bg='#040405', font=('yu gothic ui', 13, 'bold'), fg='#4F4E4D')
Self.username_label.place(x=550, y=300)

Self.username_entry = Entry(Self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#040405', font=('yu gothic ui', 13, 'bold'), fg='#4F4E4D')

Self.username_entry.place(x=580, y=330, width=270)
Self.username_line = Canvas(Self.lgn_frame, width=300, height=2.0, bg='bdb9b1', highlightthickness=0)
Self.username_line.place(x=550, y=359)


# ============= Username Icon ===============
Self.username_icon = Image.open('images\\39a1eb1485516800d84981a72840d60e.jpeg')
photo = ImageTk.PhotoImage(Self.side_image)
Self.side_image_label.image = photo
Self.side_image_label.place(x=5, y=100)
photo = ImageTk.PhotoImage



def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()


if __name__ == '__main__':
    page()
