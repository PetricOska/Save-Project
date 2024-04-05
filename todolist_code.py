import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QDialog, QDesktopWidget, QProgressBar, QMessageBox, QDialogButtonBox, QScrollArea, QTextEdit, QDateEdit  # QDateEdit 추가
from PyQt5.QtCore import QTimer, Qt, QDate  
import mysql.connector
from mysql.connector import Error

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
       
        self.setWindowTitle('어서오세요 주인님(o_o)')
        self.resize(600, 400)  

        
        layout = QVBoxLayout()

       
        welcome_label = QLabel('어서오세요 주인님(o_o)')
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet('font-size: 45px; font-weight: bold;')
        layout.addWidget(welcome_label)

        
        self.loading_bar = QProgressBar()
        self.loading_bar.setRange(0, 100)
        self.loading_bar.setValue(0)
        layout.addWidget(self.loading_bar)

        self.setLayout(layout)


        self.loading_progress = 0
        self.loading_timer = QTimer(self)
        self.loading_timer.timeout.connect(self.update_loading)
        self.loading_timer.start(20)  

      
        self.center()

   
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

 
    def update_loading(self):
        self.loading_progress += 1
        self.loading_bar.setValue(self.loading_progress)

        if self.loading_progress == 100:
            self.loading_timer.stop()
            self.show_main_page()  

  
    def show_main_page(self):
        self.loading_bar.hide()
        self.todo_app = TodoApp()
        self.todo_app.show()
        self.close()



class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
   
        self.setWindowTitle('개인비서 뽀롱이')
        self.resize(960, 700)  
        self.layout = QVBoxLayout()

     
        scroll_area = QScrollArea()  
        scroll_area.setWidgetResizable(True)  

    
        self.table = QTableWidget()
        self.table.setColumnCount(6)  
        self.table.setHorizontalHeaderLabels(['순서', '이름', '제목', '날짜', '할 일', '삭제']) 
        scroll_area.setWidget(self.table)  
        self.layout.addWidget(scroll_area) 

       
        self.add_task_btn = QPushButton('( O ㅅO)/  퀘스트 추가하기')
        self.layout.addWidget(self.add_task_btn)

        self.add_task_btn.clicked.connect(self.show_add_task_dialog)  

        self.setLayout(self.layout)

        self.show_tasks()  

       
        self.center()

   
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

   
    def show_tasks(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="todo_app"
            )

            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tasks")
                tasks = cursor.fetchall()

                self.table.setRowCount(len(tasks))
                for i, task in enumerate(tasks):
                
                    order_button = QPushButton(str(i + 1))  
                    order_button.clicked.connect(lambda _, row=i: self.show_task_details(row))  
                    self.table.setCellWidget(i, 0, order_button)  

                    for j, item in enumerate(task[1:]):  
                        self.table.setItem(i, j+1, QTableWidgetItem(str(item)))

                   
                    delete_button = QPushButton('삭제')
                    delete_button.clicked.connect(lambda _, row=i: self.confirm_delete(row))
                    self.table.setCellWidget(i, 5, delete_button)  

                conn.close()

        except Error as e:
            print(f"에러 발생: {e}")

   
    def confirm_delete(self, row):
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setWindowTitle('할 일 삭제')
        confirm_dialog.setText('( ㅇ ㅅㅇ)/  주인님 정말 삭제하실건가욥?')
        confirm_dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirm_dialog.buttonClicked.connect(lambda button: self.delete_task(row) if button.text() == 'OK' else None)
        confirm_dialog.exec()

 
    def delete_task(self, row):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="todo_app"
            )

            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT task_id FROM tasks")
                task_ids = cursor.fetchall()
                task_id = task_ids[row][0]

                
                cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
                conn.commit()  
                conn.close() 

                
                self.show_tasks()
                QMessageBox.information(self, "알림", "(ㅡㅅㅡ) 주인님 고생하셨습니다...", QMessageBox.Ok)

        except Error as e:
            print(f"에러 발생: {e}")

   
    def show_task_details(self, row):
        dialog = QDialog()
        dialog.setWindowTitle("할 일 내용")
        dialog.setFixedSize(700, 500)  
        layout = QVBoxLayout()

       
        text_edit = QTextEdit()
        text_edit.setPlainText(f"이름: {self.table.item(row, 1).text()}\n제목: {self.table.item(row, 2).text()}\n날짜: {self.table.item(row, 3).text()}\n할 일: {self.table.item(row, 4).text()}")
        text_edit.setReadOnly(True)
        text_edit.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_edit)

        dialog.setLayout(layout)
        dialog.exec()

  
    def show_add_task_dialog(self):
        self.add_task_dialog = AddTaskDialog(parent=self)  
        self.add_task_dialog.exec()


class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('할 일 추가')
        self.resize(658, 600)

        layout = QVBoxLayout()

      
        self.user_id_label = QLabel('이름')
        self.user_id_input = QLineEdit()
        layout.addWidget(self.user_id_label)
        layout.addWidget(self.user_id_input)

       
        self.title_label = QLabel('제목')
        self.title_input = QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)

      
        self.date_label = QLabel('날짜')
        self.date_input = QDateEdit(calendarPopup=True) 
        self.date_input.setDate(QDate.currentDate())  
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)

      
        self.content_label = QLabel('할 일')
        self.content_input = QLineEdit()
        layout.addWidget(self.content_label)
        layout.addWidget(self.content_input)

      
        self.add_btn = QPushButton('( O ㅅO)/  다 적으시면 말씀해주세요.')
        layout.addWidget(self.add_btn)

        self.add_btn.clicked.connect(self.add_task)

        self.setLayout(layout)

 
    def add_task(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="todo_app"
            )

            if conn.is_connected():
                cursor = conn.cursor()
               
                sql = "INSERT INTO tasks (user_id, title, date_time, content) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (
                    self.user_id_input.text(),
                    self.title_input.text(),
                    self.date_input.date().toString(Qt.ISODate),  
                    self.content_input.text()
                ))
                conn.commit()  
                conn.close()  

              
                self.parent().show_tasks()
                QMessageBox.information(self, "알림", "( º ㅅº)/  고생하세요 주인님", QMessageBox.Ok)

                self.close()  

        except Error as e:
            print(f"에러 발생: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome_page = WelcomePage()
    welcome_page.show()
    sys.exit(app.exec_())
