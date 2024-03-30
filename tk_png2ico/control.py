from ui import Win 
from tkinter import filedialog
from PIL import Image
from tkinter import messagebox
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    def __init__(self):   
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def begin_conveter(self,evt):
        # 开始转换
        #将获取到的图片转换为ico
        #我需要判断按钮组当前的值，来选择转换的尺寸
        size = 32
        if self.ui.var.get() == 2:
            size = 48
        elif self.ui.var.get() == 3:
            size = 64
        ico_path = filedialog.asksaveasfilename(defaultextension='.ico', filetypes=[('ICO Images', '*.ico')])
        img = Image.open(self.ui.file_path)
        img = img.resize((size,size))
        img.save(ico_path)
        #提示转换成功
        messagebox.showinfo('提示','转换成功')  
        
    def load_file(self,evt):
        # 从电脑中选择文件
        self.ui.file_path = filedialog.askopenfilename(filetypes=[('PNG Images', '*.png')])
        
      