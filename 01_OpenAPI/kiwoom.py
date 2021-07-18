from PyQt5.QtWidgets import *

class Kiwoom(QAxWidget):
  def __init__(self):
    super().__init__()
    print("Kiwoom Class 입니다.")
    
  def get_ocx(self):
    self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
