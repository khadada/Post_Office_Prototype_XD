# imports
from tkinter import *
from PIL import Image,ImageTk
# style 
bgc="#61BDFA" 
title_font = ('Dubai',24,'bold')
# main screen
master = Tk()
master.title('برنامج متابعة العمليات')
master.resizable(False,False)
master.config(bg=bgc,padx=20,pady=20)
# functions


# labels
Label(master,bg=bgc,text=':المبلغ الإجمالي ').grid(row=0,column=4)
total_result = Label(master,bg=bgc,text="0.0")
total_result.grid(row=1,column=4) 
Label(master,bg=bgc,text=":الملبغ المتبقي").grid(row=0,column=0)
remaining_show=Label(master,bg=bgc,text="0.0")
remaining_show.grid(row=1,column=0)
Label(master,bg=bgc,text='مرحبا بك يا خديجة في برنامجك',pady=20,font=title_font).grid(row=2,column=1,columnspan=3)
Label(master,text='البرنامج من تصميم وإنجار مليزي خالد سنة 2021',bg=bgc).grid(row=6,column=0,columnspan=5,pady=(80,0))
# frame
two_row_btn = Frame(master,width=120,bg=bgc)
two_row_btn.grid(row=4,column=1,columnspan=3,pady=40)
# Buttons
Button(master,text='إضافة مبلغ',width=20,pady=10).grid(row=3,column=3,padx=10)
Button(master,text='سحب مبلغ',width=20,pady=10).grid(row=3,column=2,padx=10)
Button(master,text='دفع مبلغ',width=20,pady=10).grid(row=3,column=1,padx=10)
Button(two_row_btn,text='مسح البيانات',width=33,pady=10).grid(row=0,column=1,padx=10)
Button(two_row_btn,text='عرض البيانات',width=33,pady=10).grid(row=0,column=0,padx=10)
Button(master,text=' إسترجاع البيانات من أخر حصة',width=70,pady=10).grid(row=5,column=1,columnspan=3)
master.mainloop()