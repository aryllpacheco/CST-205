#Aryll CST205 10/9/24
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property

# my_app = QApplication([])

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         label = QLabel()

#         self.show()

# class ButtonOne(QWidget):
#   def __init__(self):
#       super().__init__()
#       vbox = QVBoxLayout()
#       my_btn1 = QPushButton('button 1')
#       my_btn2 = QPushButton('button 2')
#       self.my_lbl1 = QLabel('button not yet clicked')
#       self.my_lbl2 = QLabel('button not yet clicked')
#       my_btn1.clicked.connect(self.on_click)
#       my_btn2.clicked.connect(self.on_click2)
#       vbox.add_widget(self.my_lbl1)
#       vbox.add_widget(self.my_lbl2)
#       vbox.add_widget(my_btn1)
#       vbox.add_widget(my_btn2)
#       self.set_layout(vbox)
#       self.resize(400, 400)
#       self.show()

#   @Slot()
#   def on_click(self):
#       self.my_lbl1.text = 'button 1 has been clicked!'
#   @Slot()
#   def on_click2(self):
#       self.my_lbl2.text = 'button 2 has been clicked!'

# my_win = ButtonOne()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.my_lbl = QLabel('CST 205 Color Exchange!')

        self.my_list = ["Pick a value", "red", "green", "blue", "yellow"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_lbl)
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        color_list = ['', '(255,0,0)', '(0,255,0)', '(0,0,255)', '(255,255,0)']
        color_list_hex = ['', '#FF0000', '#0000FF', '#00FF00', '#FFFF00']
        curr_index = self.my_combo_box.current_index
        self.my_label.text = f'RGB {color_list[curr_index]}         Hex {color_list_hex[curr_index]}'


app = QApplication([])
my_win = MyWindow()
my_win.show()

sys.exit(app.exec())