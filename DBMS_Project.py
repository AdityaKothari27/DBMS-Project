import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import mysql.connector


class welcomescreen(QDialog):
    def __init__(self):
        super(welcomescreen, self).__init__()
        loadUi("/Users/adityakothari/Desktop/Python/untitled.ui", self)
        self.pushButton.clicked.connect(self.gotoutput)
        self.quit.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_2.clicked.connect(self.gototable1)
        self.pushButton_3.clicked.connect(self.gototable2)
        self.pushButton_4.clicked.connect(self.gototable3)
        self.pushButton_5.clicked.connect(self.gototable4)
        self.pushButton_6.clicked.connect(self.gototable5)
        self.pushButton_7.clicked.connect(self.gototable6)
        self.pushButton_8.clicked.connect(self.gototable7)
        self.pushButton_9.clicked.connect(self.gototable8)
        self.pushButton_10.clicked.connect(self.gototable9)
        self.pushButton_11.clicked.connect(self.gototable10)
        self.pushButton_12.clicked.connect(self.gototable11)
        self.pushButton_13.clicked.connect(self.gototable12)
        self.pushButton_14.clicked.connect(self.gototable13)
        self.pushButton_15.clicked.connect(self.gototable14)


    def gotoutput(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = self.lineEdit.text()

        cursor.execute(query)

        result = cursor.fetchall()
        print(cursor.statement)
        print(result)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.commit()

    def gototable1(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc passenger"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable2(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc aircraft"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable3(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root', password='Aditya@11')
        cursor = db.cursor()
        query = "desc stores"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def gototable4(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc airline"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def gototable5(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc departures"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable6(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc lounge"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable7(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc international"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable8(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc ticket"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable9(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc arrivals"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable10(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc assistance"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable11(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc domestic"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable12(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc employee"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable13(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc parking"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def gototable14(self):
        db = mysql.connector.connect(host='localhost', database='airport_management', user='root',
                                     password='Aditya@11')
        cursor = db.cursor()
        query = "desc luggage"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


# main
app = QApplication(sys.argv)
welcome = welcomescreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1440)
widget.setFixedHeight(1080)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")