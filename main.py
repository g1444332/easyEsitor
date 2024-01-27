from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QFileDialog
import os

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Easy Editor")
main_win.resize(700, 400)

btn_dir = QPushButton("Папка")
lb_image = QLabel("Картинка")
lw_files = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")


row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

workdir = ''

def filter(files, extension):
    result = []
    for filename in files:
        for ext in extension:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extension = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    try:
        filenames = filter(os.listdir(workdir), extension)
        lw_files.clear()
        for filename in filenames:
            lw_files.addItem(filename)
    except FileNotFoundError:
        pass

btn_dir.clicked.connect(showFilenamesList)



main_win.setLayout(row)
main_win.show()
app.exec_()