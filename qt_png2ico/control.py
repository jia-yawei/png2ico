from ui_ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PIL import Image
#定义一个打开文件的函数
class Controller:
    def __init__(self):
        self.app = QApplication([])
        self.MainWindow = QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.MainWindow)
        self.ui.pushButton.clicked.connect(self.handle_button_click) 
        self.ui.pushButton_2.clicked.connect(self.convert_button_click)  
    def show(self):
        self.MainWindow.show()
        self.app.exec_()
    def handle_button_click(self):
        #打开文件对话框,选择一个png文件,不要局部变量，否则会被释放
        self.filename, _ = QFileDialog.getOpenFileName(None, 'Open file', '', 'Image files (*.png)')
        if not self.filename:
            return
        #filename是文件的路径，取出文件的名字
        name = self.filename.split("/")[-1]
        #将文件名显示在label上
        self.ui.label_2.setText(name) 
    def convert_button_click(self):
        #将png文件转换为ico格式，可以选择设置的尺寸，保存在当前目录
        img = Image.open(self.filename)
        #将文件名的后缀改为ico

        #判断是否有尺寸设置
        if self.ui.radioButton.isChecked():
            size = (48, 48)
        elif self.ui.radioButton_2.isChecked():
            size = (64, 64)
        elif self.ui.radioButton_3.isChecked():
            size = (128, 128)
        ico_name, _ = QFileDialog.getSaveFileName(self.MainWindow, "保存文件", "", "Icon Files (*.ico)")
        img = img.resize(size)
        img.save(ico_name)
        QMessageBox.information(self.MainWindow, "提示", "转换成功")    

       
        

        
        

        



   