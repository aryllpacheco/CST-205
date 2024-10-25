#Aryll Pacheco CST205 10/14/24
#A GUI that gives the user the oppurunity to send in a search term to find an image and apply a filter to it
import sys
from PIL import Image
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox,
QLineEdit)
from PySide6.QtCore import (Slot, Qt)
from PySide6.QtGui import QPixmap
from functions import my_search
from __feature__ import snake_case, true_property

my_app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.my_lbl = QLabel('Image Manipulation Filter')

        self.line_edit = QLineEdit()
        self.line_edit.placeholder_text = "Enter Search Term"


        self.my_list = ["Pick a filter", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")

        self.btt1 = QPushButton()

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_lbl)
        vbox.add_widget(self.line_edit)
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)
        vbox.add_widget(self.btt1)

        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        selected_filter = self.my_combo_box.current_text
        if selected_filter == 'Grayscale':
            self.Grayscale()
        elif selected_filter == 'Sepia':
            self.Sepia()
        elif selected_filter == 'Negative':
            self.Negative()
        elif selected_filter == 'Thumbnail':
            self.Thumbnail()
        elif selected_filter == 'None':
            self.curr_img = my_search(self.line_edit.text)
            if self.curr_img == "no_results":
                self.curr_img = Image.open("hw3_images/no_results.jpg") 
            else:
                self.curr_img = Image.open(f"hw3_images/{self.curr_img}.jpg")
            self.curr_img.show()

    def Grayscale(self):
        self.curr_img = my_search(self.line_edit.text)
        if self.curr_img == "no_results":
            self.curr_img = Image.open("hw3_images/no_results.jpg")  
        else:
            self.curr_img = Image.open(f"hw3_images/{self.curr_img}.jpg")
        new_list = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000,) * 3 for a in self.curr_img.getdata()]
        self.curr_img.putdata(new_list)
        self.curr_img.show()

    def Sepia(self):
        self.curr_img = my_search(self.line_edit.text)
        if self.curr_img == "no_results":
            self.curr_img = Image.open("hw3_images/no_results.jpg") 
        else:
            self.curr_img = Image.open(f"hw3_images/{self.curr_img}.jpg")
        sepia_list = []

        for p in self.curr_img.getdata():
            if p[0] < 63:
                r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
                
            elif p[0] > 62 and p[0] < 192:
                r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
                
            else:
                r = int(p[0] * 1.08)
                g,b = p[1], int(p[2] * 0.5)
      
            sepia_list.append((r,g,b))

        self.curr_img.putdata(sepia_list)
        self.curr_img.show()
        

    def Negative(self):
        self.curr_img = my_search(self.line_edit.text)
        if self.curr_img == "no_results":
            self.curr_img = Image.open("hw3_images/no_results.jpg") 
        else:
            self.curr_img = Image.open(f"hw3_images/{self.curr_img}.jpg")
        negative_list = [(255-p[0], 255-p[1], 255-p[2])
                           for p in self.curr_img.getdata()]
        self.curr_img.putdata(negative_list)
        self.curr_img.show()

    def Thumbnail(self):
        self.curr_img = my_search(self.line_edit.text)
        if self.curr_img == "no_results":
            self.curr_img = Image.open("hw3_images/no_results.jpg") 
        else:
            self.curr_img = Image.open(f"hw3_images/{self.curr_img}.jpg")
        w, h = self.curr_img.width//2, self.curr_img.height//2
        self.my_trgt = Image.new('RGB', (w, h))
        target_x = 0
        for source_x in range(0, self.curr_img.width, 2):
            target_y = 0
            for source_y in range(0, self.curr_img.height, 2):
                p = self.curr_img.getpixel((source_x, source_y))
                self.my_trgt.putpixel((target_x, target_y), p)
                target_y += 1
                
            target_x += 1

        self.my_trgt.show()


my_win = MyWindow()
my_win.show()

sys.exit(my_app.exec())