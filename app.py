from tkinter import *
total_amount =10

class App(Tk):
    def __init__(self,ttl=' Post Office',bgc="#61BDFA"):
        super().__init__()
        self.config(padx=60,pady=60)
        self.title(ttl)
        self.logo = PhotoImage(file='imgs\post_office_logo.png')
        self.iconphoto(False, self.logo)
        self.bgc = bgc
        self.config(bg=bgc)
        self.resizable(False,False)
        
    
    def setup_app(self):
        bgc = self.bgc
        total_amount_label = Label(self,bg=bgc,text=':المبلغ الإجمالي ')
        total_amount_label.grid(row=0,column=4)
        total_amount_show = Label(self,bg=bgc,text=' 0.0 Da')
        total_amount_show.grid(row=1,column=4) 
        remaining_amount_label = Label(self,bg=bgc,text=":الملبغ المتبقي")
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
        
        
    def add_amount(self):
        def confirm_msg():
            
            default_txt = f"هل أنت متأكدة من إضافة المبلغ : {add_amount_input.get()} دج"
            error = "تأكدي من القيمة "
                
            
            msg_pop = Toplevel(amount_win,padx=20,pady=20)
            
            msg_text = Label(msg_pop ,text=default_txt)
            img = None
            if len(add_amount_input.get()) > 0 and isinstance(int(add_amount_input.get()),int):
                img = '::tk::icons::question'
                
            else:
                img = '::tk::icons::error'
                msg_text.config(text=error)
            canvas = Canvas(msg_pop,width=50,height=50,highlightthickness=0)
            canvas.grid(row=0,column=0)
            canvas.create_image(25,25,image=img)
            msg_text.grid(row=0,column=1,columnspan=3)
            def yes_answer():
                msg_pop.destroy()
                ok_btn.config(state=NORMAL)
                return True
            def no_answer():
                ok_btn.config(state=DISABLED)
                msg_pop.destroy()
                return False
            yes_btn = Button(msg_pop,text="نعم",width=15,pady=10,command=yes_answer)
            yes_btn.grid(row=1,column=2)
            no_btn = Button(msg_pop,text="لا",width=15,pady=10,command=no_answer)
            no_btn.grid(row=1,column=3)
                
            msg_pop.mainloop()
        amount_win = Tk()
        amount_win.config(padx=60,pady=60,bg=self.bgc)
        add_amount_title = Label(amount_win,text="إضافة مبلغ إلي الرصيد الإجمالي",bg=self.bgc)
        add_amount_title.grid(row=0,column=0,columnspan=3)
        add_amount_input=Entry(amount_win,width=50,borderwidth=15,relief=FLAT)
        add_amount_input.grid(row=1,column=1,columnspan=2,pady=50)
        currency_label = Label(amount_win,text="دج",bg=self.bgc)
        currency_label.grid(row=1,column=0,padx=10)
        confirm_amount_btn = Button(amount_win,text="تأكيد العملية",width=20,pady=10,command=confirm_msg)
        confirm_amount_btn.grid(row=2,column=2,padx=(10,0))
        def set_add_amount():
            global total_amount
            total_amount += int(add_amount_input.get())
            amount_win.destroy()
            
            
        ok_btn = Button(amount_win,text=" موافـــق",width=20,pady=10,state=DISABLED,command=set_add_amount)
        ok_btn.grid(row=2,column=1,padx=(0,10))
        
            
        
        amount_win.mainloop()
        
    def keep_win_open(self):
        self.mainloop()
    
    
    

app = App()
app.setup_app()
app.add_amount()
app.keep_win_open()
print(f'the total amount you have = {total_amount}')