#Aryll CST205 10/14/24
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox)
from PySide6.QtCore import (Slot, Qt)
from PySide6.QtGui import QPixmap
from __feature__ import snake_case, true_property

my_app = QApplication([])

'''This class creates a new window and changes the background color of the window to cyan'''
class backgroundWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.windowTitle = 'color'
        self.palette = Qt.cyan

'''This class is creating a new window and changing the layout in which the buttons are showing up 
on the screen for the user to interact with'''
class nestedWindow(QWidget):
    def __init__(self):
        super().__init__()

        v_layout = QVBoxLayout()
        b1 = QPushButton('Green')
        b2 = QPushButton('Yellow')

        v_layout.add_widget(b1)
        v_layout.add_widget(b2)

        h_layout = QHBoxLayout()
        b3 = QPushButton('Peach')

        h_layout.add_widget(b3)

        b4 = QPushButton('Cyan')
        b5 = QPushButton('Purple')

        v_layout.add_widget(b4)
        v_layout.add_widget(b5)
        
        main_layout = QHBoxLayout()

        main_layout.add_layout(v_layout)
        main_layout.add_layout(h_layout)
        self.set_layout(main_layout)
        

class ShowColor(QWidget):
    def __init__(self):
        super().__init__()

        self.my_list = ["Pick a value", "red", "green", "blue", "yellow"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_label)
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        color_list = ['', '(255,0,0)', '(0,255,0)', '(0,0,255)', '(255,255,0)']
        color_list_hex = ['', '#FF0000', '#0000FF', '#00FF00', '#FFFF00']
        curr_index = self.my_combo_box.current_index
        b1 = QPushButton('Make new color window')
        main_layout = QHBoxLayout()
        main_layout.add_widget(b1)
        self.set_layout(main_layout)   

    class backgroundWindow(QWidget):
        def __init__(self, color):
            super().__init__()

            self.windowTitle = 'color'
            self.palette = color   

# I was working on making sure that the window would open properly
# when I was working on it I initially got the drop down menu working and the corlor that are options
# I did end up running of time before I was able to get the menu to work and open up a new window 
# with the color that was selected by the user

my_window = ShowColor()
my_window.show()

sys.exit(my_app.exec())