from tkinter import *
class App(Tk):
    def __init__(self,ttl=' Post Office',bgc="#61BDFA"):
        super().__init__()
        self.config(padx=60,pady=60)
        self.title(ttl)
        self.logo = PhotoImage(file='imgs\post_office_logo.png')
        self.iconphoto(False, self.logo)
        self.bgc = bgc
        self.config(bg=bgc)
        
    
    def setup_app(self):
        bgc = self.bgc
        total_amount_label = Label(self,bg=bgc,text='المبلغ الإجمالي: ')
        total_amount_label.grid(row=0,column=4)
        total_amount_show = Label(self,bg=bgc,text=' 0.0 Da')
        total_amount_show.grid(row=1,column=4)
        
        
        remaining_amount_label = Label(self,bg=bgc,text="الملبغ المتبقي")
        remaining_amount_label.grid(row=0,column=0)
        remaining_amount_show = Label(self,bg=bgc,text='  0.0 Da')
        remaining_amount_show.grid(row=1,column=0)
        
        
        hi_client = Label(self,bg=bgc,text='مرحبا بك يا خديجة في برنامجك',pady=20)
        hi_client.grid(row=2,column=1,columnspan=3)
        
        
        add_amount_btn = Button(self,text='إضافة مبلغ',width=20,pady=10)
        add_amount_btn.grid(row=3,column=3,padx=10)
        
        pull_amount_btn = Button(self,text='سحب مبلغ',width=20,pady=10)
        pull_amount_btn.grid(row=3,column=2,padx=10)
        
        
        push_amount_btn = Button(self,text='دفع مبلغ',width=20,pady=10)
        push_amount_btn.grid(row=3,column=1,padx=10)
        
        two_row_btn = Frame(self,width=120,bg=bgc)
        two_row_btn.grid(row=4,column=1,columnspan=3,pady=40)
        
        clean_info_btn = Button(two_row_btn,text='مسح البيانات',width=33,pady=10)
        clean_info_btn.grid(row=0,column=1,padx=10)
        get_info_btn = Button(two_row_btn,text='عرض البيانات',width=33,pady=10)
        get_info_btn.grid(row=0,column=0,padx=10)
        
        restore_info_btn =Button(self,text=' إسترجاع البيانات من أخر حصة',width=70,pady=10)
        restore_info_btn.grid(row=5,column=1,columnspan=3)
        
        footer = Label(self,text='البرنامج من تصميم وإنجار مليزي خالد سنة 2021',bg=bgc)
        footer.grid(row=6,column=0,columnspan=5,pady=(80,0))
        
        
    
    def keep_win_open(self):
        self.mainloop()
    
    
    

app = App()
app.setup_app()
app.keep_win_open()