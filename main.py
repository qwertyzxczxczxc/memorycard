from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QFileDialog
import os
from PyQt5.QtGui import QPixmap 
from PIL import Image, ImageFilter


app = QApplication([])



window = QWidget()
window.setWindowTitle('Умные заметки')
btn_dir = QPushButton("папка")
btn_left = QPushButton("лево")
btn_right = QPushButton("право")
btn_mirrow = QPushButton("зеркало")
btn_fg = QPushButton("резкость")
btn_hb = QPushButton("Ч/Б")
lw_files = QListWidget()
lb_image = QLabel("Картинка")

window.resize(700, 500)
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()

col_2.addWidget(lb_image)
col_1.addWidget(btn_dir)
row_2.addWidget(btn_left)
row_2.addWidget(btn_right)
row_2.addWidget(btn_mirrow)
row_2.addWidget(btn_fg)
row_2.addWidget(btn_hb)
row_1.addLayout(col_1)
col_1.addWidget(lw_files)
col_2.addLayout(row_2)
row_1.addLayout(col_2)






window.setLayout(row_1)
window.show()

workdir = ''
def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
def showFilenamesList():
    extensions = [".jpg ",".jpeg",".png","gif",".bmp"]
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self):
        self.Image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path) 

def showChosenImage():
      if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

    



workimage = ImageProcessor() 
lw_files.currentRowChanged.connect(showChosenImage)

btn_hb.clicked.connect(workimage.do_bw)
btn_mirrow.clicked.connect(workimage.do_flip)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_fg.clicked.connect(workimage.do_blur)





app.exec()