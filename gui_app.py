# imports
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
# style "#61BDFA"
bgc="#ffb6b6" 
title_font = ('Dubai',24,'bold')
btn_font = ('Dubai',14,'normal')
sub_title_font = ('Dubai',14,'normal')
entry_font = ('Dubai',30,'normal')
currency_font = ('Dubai',38,'normal')
msg_font = ('Dubai',18,'normal')
msg_bgc = '#61BDFA'
# vars

# functions
def confim(win,msg):     
    message_box = Toplevel(win)
    message_box.resizable(False,False)
    message_box.config(pady=20,padx=40,bg=msg_bgc)
    message_box.title('confirm')
    letter = Label(message_box,text=msg,font=msg_font,bg=msg_bgc)
    letter.grid(row=0,column=0,columnspan=2,pady=20)
    # buttons
    def ok_fired():
        message_box.destroy()
        ok_btn.config(state=NORMAL)
    yes_btn=Button(message_box,text="نـعـم",width=20,pady=10,font=btn_font,command=ok_fired)
    yes_btn.grid(row=1,column=0)
    Button(message_box,text="تراجـع",width=20,pady=10,font=btn_font,command=message_box.destroy).grid(row=1,column=1)

def set_amount():
    old_val = total_result.cget("text") 
    if old_val =="0.0":
        old_val = 0    
    total = int(old_val) + int(amount.get())
    total_result.config(text=total) 
    add_amount_screen.destroy()
def add_amount():
    global amount
    global add_amount_screen
    global ok_btn
    amount = StringVar()
    add_amount_screen = Toplevel(master)
    add_amount_screen.title('إضـــافة مبـــلغ')
    add_amount_screen.config(padx=20,pady=20,bg=bgc)
    # labels
    Label(add_amount_screen,text="نافذة إضافة مبلغ إلى الرصيد الإجمالي", font=title_font,bg=bgc,justify=CENTER).grid(row=0,column=0,columnspan=3,pady=(0,60))
    Label(add_amount_screen,text="دج",font=currency_font,bg=bgc).grid(row=1,column=0,padx=(0,15))
    # entry
    Entry(add_amount_screen,borderwidth=15,relief=FLAT,textvariable=amount,width=20,font=entry_font,justify=CENTER).grid(row=1,column=1,columnspan=2)
    # frame
    two_row_btn = Frame(add_amount_screen,width=100,bg=bgc)
    two_row_btn.grid(row=2,column=1,columnspan=2,pady=40)
    # buttons
    def turn_on():
        response = messagebox.askquestion('message','هل انت متأكدة')
        if response=="yes":
            ok_btn.config(state=NORMAL)
    Button(two_row_btn,text='التأكــد',width=30,pady=15,font=btn_font,command=turn_on).grid(row=2,column=1,padx=(0,20))
    ok_btn=Button(two_row_btn,text=' موافــق',width=30,pady=15,font=btn_font,state=DISABLED,command=set_amount)
    ok_btn.grid(row=2,column=2,padx=(0,20))

# main screen
master = Tk()
master.title('برنامج متابعة العمليات')
master.resizable(False,False)
master.config(bg=bgc,padx=20,pady=20)
# labels
Label(master,bg=bgc,text=':المبلغ الإجمالي ',font=sub_title_font).grid(row=0,column=4)
total_result = Label(master,bg=bgc,text="0.0",font=sub_title_font)
total_result.grid(row=1,column=4) 
Label(master,bg=bgc,text=":الملبغ المتبقي",font=sub_title_font).grid(row=0,column=0)
remaining_show=Label(master,bg=bgc,text="0.0",font=sub_title_font)
remaining_show.grid(row=1,column=0)
Label(master,bg=bgc,text='مرحبا بك يا خديجة في برنامجك',pady=20,font=title_font).grid(row=2,column=1,columnspan=3)
Label(master,text='البرنامج من تصميم وإنجار مليزي خالد سنة 2021',bg=bgc).grid(row=6,column=0,columnspan=5,pady=(80,0))
# frame
two_row_btn = Frame(master,width=120,bg=bgc)
two_row_btn.grid(row=4,column=1,columnspan=3,pady=40)
# Buttons
Button(master,text='إضافة مبلغ',width=20,pady=10,font=btn_font,command=add_amount).grid(row=3,column=3,padx=10)
Button(master,text='سحب مبلغ',width=20,pady=10,font=btn_font).grid(row=3,column=2,padx=10)
Button(master,text='دفع مبلغ',width=20,pady=10,font=btn_font).grid(row=3,column=1,padx=10)
Button(two_row_btn,text='مسح البيانات',width=33,pady=10,font=btn_font).grid(row=0,column=1,padx=10)
Button(two_row_btn,text='عرض البيانات',width=33,pady=10,font=btn_font).grid(row=0,column=0,padx=10)
Button(master,text=' إسترجاع البيانات من أخر حصة',width=70,pady=10,font=btn_font).grid(row=5,column=1,columnspan=3)
master.mainloop()