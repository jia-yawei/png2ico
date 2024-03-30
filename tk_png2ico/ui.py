"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import Tk,Button,Radiobutton,IntVar,Label,Scrollbar
from tkinter.ttk import Style
class WinGUI(Tk):
    def __init__(self): 
        super().__init__()
        self.__win()
        self.tk_button_button_conveter = self.__tk_button_button_conveter(self)
        self.tk_button_button_openfile = self.__tk_button_button_openfile(self)
        self.tk_radio_button_radio_32xs = self.__tk_radio_button_radio_32xs(self)
        self.tk_radio_button_radio_48xs = self.__tk_radio_button_radio_48xs(self)
        self.tk_radio_button_radio_64xs = self.__tk_radio_button_radio_64xs(self)
        self.tk_label_label_tltle = self.__tk_label_label_tltle(self)
        self.__set_button_group()
    def __win(self):
        self.title("Png转ico小工具")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)     
        self.resizable(width=False, height=False)   

    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_button_button_conveter(self,parent):
        btn = Button(parent, text="转换", takefocus=False,)
        btn.place(x=189, y=362, width=130, height=30)
        return btn
    def __tk_button_button_openfile(self,parent):
        btn = Button(parent, text="打开文件", takefocus=False,)
        btn.place(x=190, y=120, width=115, height=30)
        return btn
    def __tk_radio_button_radio_32xs(self,parent):
        rb = Radiobutton(parent,text="32像素",)
        rb.place(x=204, y=203, width=112, height=30)
        return rb
    def __tk_radio_button_radio_48xs(self,parent):
        rb = Radiobutton(parent,text="48像素",)
        rb.place(x=204, y=244, width=112, height=30)
        return rb
    def __tk_radio_button_radio_64xs(self,parent):
        rb = Radiobutton(parent,text="64像素",)
        rb.place(x=204, y=285, width=112, height=30)
        return rb

    def __set_button_group(self):
        self.var = IntVar()
        self.tk_radio_button_radio_32xs.config(variable=self.var, value=1)  
        self.tk_radio_button_radio_48xs.config(variable=self.var, value=2)  
        self.tk_radio_button_radio_64xs.config(variable=self.var, value=3)
    def __tk_label_label_tltle(self,parent):
        label = Label(parent,text="Png转ico小工具",anchor="center", )
        #设置字体
        ft = ('微软雅黑', 20)
        label.configure(font=ft)
        #设置字体颜色
        label.configure(foreground="#000000")
        #设置背景颜色
        label.configure(background="#d9d9d9")

        label.place(x=174, y=21, width=239, height=45)
        return label
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_button_openfile.bind('<Button-1>',self.ctl.load_file)
        self.tk_button_button_conveter.bind('<Button-1>',self.ctl.begin_conveter)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()