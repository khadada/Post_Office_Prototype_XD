from tkinter import *
class App(Tk):
    def __init__(self,ttl=' Post Office'):
        super().__init__()
        self.config(padx=40,pady=40)
        self.title(ttl)
        self.logo = PhotoImage(file='imgs\post_office_logo.png')
        self.iconphoto(False, self.logo)
        
    
    def keep_win_open(self):
        self.mainloop()
    
    

app = App()
app.keep_win_open()