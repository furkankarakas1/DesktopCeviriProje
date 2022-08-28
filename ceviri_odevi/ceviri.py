
import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem ,QHeaderView,QCompleter
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Login(QDialog):

    def __init__(self):
        super(Login,self).__init__()
        loadUi("firstW.ui",self)  
        

        self.engToTr_2.clicked.connect(self.loginfunction)
        self.trToEng_2.clicked.connect(self.loginfunction2)

    def loginfunction(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
 

    def loginfunction2(self):
        createacc2 = CreateAcc2()
        widget.addWidget(createacc2)
        widget.setCurrentIndex(widget.currentIndex()+1)            





class CreateAcc(QDialog):
    
 

    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("englishTurkish.ui",self)
        sentences = ('come','here','because','im','about','crazy','hello','car','dude')     
        
        autocomp=QCompleter(sentences)
        

        self.okbtn.clicked.connect(self.find)
        self.lineEditGirdi.setCompleter(autocomp)

        companies = ('come','here','because','im','about','crazy')
        model = QStandardItemModel(len(companies), 1)
        model.setHorizontalHeaderLabels(['English Sentences'])  

        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)

        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        self.lineEditGirdi.textChanged.connect(filter_proxy_model.setFilterRegExp)

        self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(filter_proxy_model)

        


    def find(self):     


        with open("jey.json") as f:
            data = json.load(f)   
        

        sentence = self.lineEditGirdi.text()

        words = sentence.lower().split()

        for word in words:
            wordMeaning = data.get(word.lower(),"anlam bulunuamadı")
            print(f'{word}  :  {wordMeaning}')

        self.label_karsilik.setText(f'{wordMeaning}') 






class CreateAcc2(QDialog):

    def __init__(self):
        super(CreateAcc2,self).__init__()
        loadUi("turkceingilizce.ui",self)
        sentences = ('gel','burasi','cünkü','ben','cünkü','cilgin')    
        
        autocomp=QCompleter(sentences)
        

        self.okbtn.clicked.connect(self.find)
        self.lineEditGirdi.setCompleter(autocomp)

        companies = ('gel','burasi','cünkü','ben','cünkü','cilgin')    
        model = QStandardItemModel(len(companies), 1)
        model.setHorizontalHeaderLabels(['Türkçe sözcükler'])  

        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)

        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        self.lineEditGirdi.textChanged.connect(filter_proxy_model.setFilterRegExp)

        self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(filter_proxy_model)

        


    def find(self):     


        with open("jey2.json") as f:
            data = json.load(f)   
        

        sentence = self.lineEditGirdi.text()

        words = sentence.lower().split()

        for word in words:
            wordMeaning = data.get(word.lower(),"anlam bulunuamadı")
            print(f'{word}  :  {wordMeaning}')

        self.label_karsilik.setText(f'{wordMeaning}') 




        

app = QApplication(sys.argv)
mainwindow=Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
app.exec_() 