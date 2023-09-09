#create the Easy Editor photo editor here!

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(700,400)
window.setWindowTitle("Easy Editor app")

button_left = QPushButton('Left')
button_right = QPushButton('Right')
button_mirror = QPushButton('Mirror')
button_sharpness = QPushButton('Sharpness')
button_b_w = QPushButton('B&W')

button_folder = QPushButton('Folder')
label_pic = QLabel("")
list_widget = QListWidget()

row =QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
buttons_row = QHBoxLayout()

col1.addWidget(button_folder)
col1.addWidget(list_widget)

col2.addWidget(label_pic)
col2.addLayout(buttons_row)

buttons_row.addWidget(button_left)
buttons_row.addWidget(button_right)
buttons_row.addWidget(button_mirror)
buttons_row.addWidget(button_sharpness)
buttons_row.addWidget(button_b_w)

row.addLayout(col1)
row.addLayout(col2)
window.setLayout(row)
window.show()
app.exec()


