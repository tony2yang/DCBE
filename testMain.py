# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from combox import *
import os

import sys

class myWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        # super(myWindow, self).__init__()
        self.setupUi(self)
        self.initial_records()

    def initial_records(self):
        if os.path.isfile ("records.cfg"):
            with open('records.cfg', 'r') as f:
                for i in f.readlines():
                    #print(i.strip()) # strip() delete '/n'
                    file_path, show_name = i.strip().split(',')
                    #print(file_path, show_name)
                    self.textBrowser.append ('<a href="' + file_path +
                                             '">' + show_name + '</a>')



    def add(self):
        #self.textBrowser.append(self.lineEdit.displayText())
        file_path = self.lineEdit.displayText()
        show_name = QFileInfo(file_path).fileName()
        self.textBrowser.append('<a href="' + file_path +
                                '">'+ show_name +'</a>')

        with open('records_tmp.cfg', 'w') as f:
            f.write(file_path + ','+ show_name)
            f.write('\n')

    def file_path(self):
        open_file, file_type = QFileDialog.getOpenFileName(self,'选择文件','')
        #file_name = QFileInfo(open_file).fileName()
        self.lineEdit.setText(open_file)

    def reset(self):
        if os.path.isfile ("records.cfg"):
            os.remove('records.cfg')

    def saveRecords(self):
        if os.path.isfile("records_tmp.cfg"):
            with open('records.cfg', 'a+') as f:
                print('working: ', f.read())
                with open ('records_tmp.cfg', 'r') as tf:
                    for i in tf.readlines():
                        if i not in f.readlines():
                            f.write(i)
            os.remove('records_tmp.cfg')


if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)
    myshow=myWindow()
    myshow.show()
    sys.exit(app.exec_())
