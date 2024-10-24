from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
import pandas as pd
import os


class Login_in(QMainWindow):
    def __init__(self):
        super(Login_in, self).__init__()
        uic.loadUi('dangnhap.ui', self)
        self.okdn.clicked.connect(self.login)
        self.OKDK.clicked.connect(self.reg_from)
  
    def reg_from(self):
        widget.setCurrentIndex(1)
        return 0
    def login(self):
        name_input = self.user.text().strip()  # Lấy tên từ giao diện và loại bỏ khoảng trắng thừa
        pass_input = self.mk.text().strip()    # Lấy mật khẩu từ giao diện và loại bỏ khoảng trắng thừa)
        # Đọc dữ liệu từ file CSV
        list1 = pd.read_csv('user1.csv')
        user_exists = list1['Name'].str.contains(name_input, case=False, na=False)
        if not name_input and not pass_input :
            QMessageBox.warning(self, "Đăng nhập", "Không được để trống")
            return 
        if user_exists.any():  # Kiểm tra xem có người dùng nào khớp không
            # Lấy mật khẩu của người dùng (nếu có nhiều người khớp, sẽ lấy người đầu tiên) 
            user_password = list1.loc[user_exists, 'Pass'].values[0]  
         
            if str(user_password) == str(pass_input):
                QMessageBox.warning(self, "Đăng nhập", "Đăng nhập thành công")
                widget.setCurrentIndex(2)
            else:
                QMessageBox.warning(self, "Đăng nhập", "Sai mậ khẩu")
        else:
            QMessageBox.warning(self, "Đăng nhập", "Sai tài khoản")


class Login_up(QMainWindow):
    def __init__(self):
        super(Login_up, self).__init__()
        uic.loadUi('dangky.ui', self)
        self.okdk.clicked.connect(self.register)
        self.ql.clicked.connect(self.seg)

    def seg(self):
        widget.setCurrentIndex(0)
        return 
    def register(self):
        name_input = self.user.text().strip()
        pass_input = self.mk.text().strip()
        email_input = self.email.text().strip()
        user_input = self.name.text().strip()
        # Kiểm tra dữ liệu người dùng nhập
        if not name_input and not pass_input and not email_input and not user_input:
            QMessageBox.warning(self, "Đăng ký", "Không được để trống")
            return

        # Đọc file CSV (nếu file đã tồn tại)
        if os.path.exists('user1.csv'):
            df = pd.read_csv('user1.csv')

            # Kiểm tra xem người dùng đã tồn tại chưa
            if (df['Name'] == name_input).any():
                QMessageBox.warning(self, "Đăng ký", "Tài khoản đã tồn tại")
            else:
                # Thêm người dùng mới vào file CSV
                new_user = pd.DataFrame({'Name': [name_input], 'Pass': [pass_input], 'email': [email_input], 'user': [user_input]})
                new_user.to_csv('user1.csv', mode='a', header=False, index=False)
                QMessageBox.information(self, "Đăng ký", "Đăng ký thành công")
                widget.setCurrentIndex(2)
        else:
            # Tạo file mới nếu file chưa tồn tại và thêm người dùng
            new_user = pd.DataFrame({'Name': [name_input], 'Pass': [pass_input], 'email': [email_input], 'user': [user_input]})
            new_user.to_csv('user1.csv', mode='w', header=True, index=False)
            QMessageBox.information(self, "Đăng ký", "Đăng ký thành công")
            widget.setCurrentIndex(2)


class Main1(QMainWindow):
    def __init__(self):
        super(Main1, self).__init__()
        uic.loadUi('lich.ui', self)
        self.ql.clicked.connect(self.seg)
        self.lich.clicked.connect(self.main2)
        self.t2.clicked.connect(self.T2)
        self.t3.clicked.connect(self.T3)
        self.t4.clicked.connect(self.T4)
        self.t5.clicked.connect(self.T5)
        self.t6.clicked.connect(self.T6)
        self.t7.clicked.connect(self.T7)
        self.cn.clicked.connect(self.CN)
    def seg(self):
        widget.setCurrentIndex(0)
    def main2(self):
        widget.setCurrentIndex(3)
    def T2(self):
        widget.setCurrentIndex(4)
    def T3(self):
        widget.setCurrentIndex(5)
    def T4(self):
        widget.setCurrentIndex(6)
    def T5(self):
        widget.setCurrentIndex(7)
    def T6(self):
        widget.setCurrentIndex(8)
    def T7(self):
        widget.setCurrentIndex(9)
    def CN(self):
        widget.setCurrentIndex(10)
class Main2(QMainWindow):
    def  __init__(self):
        super(Main2, self).__init__()
        uic.loadUi('lichs.ui', self)
        self.ql.clicked.connect(self.seg)
        self.thongbao.clicked.connect(self.main1)

    def seg(self):
        widget.setCurrentIndex(0)
        return 0
    def main1(self):
        widget.setCurrentIndex(2)

class THU2(QMainWindow):
    def __init__(self):
        super(THU2, self).__init__()
        uic.loadUi('T2.ui', self)
        self.ql.clicked.connect(self.seg)
        self.ok.clicked.connect(self.OK)
        self.t3.clicked.connect(self.T3)
        self.t4.clicked.connect(self.T4)
        self.t5.clicked.connect(self.T5)
        self.t6.clicked.connect(self.T6)
        self.t7.clicked.connect(self.T7)
        self.cn.clicked.connect(self.CN)
    def seg(self):
        widget.setCurrentIndex(2)
    def T3(self):
        widget.setCurrentIndex(5)
    def T4(self):
        widget.setCurrentIndex(6)
    def T5(self):
        widget.setCurrentIndex(7)
    def T6(self):
        widget.setCurrentIndex(8)
    def T7(self):
        widget.setCurrentIndex(9)
    def CN(self):
        widget.setCurrentIndex(10)
    def OK(self):
        jod_input = self.jod.text().strip()
        status_input = self.do_2.text().strip()
        new_user = pd.DataFrame({'jod': [jod_input], 'do': [status_input]})
        new_user.to_csv('T2.csv', mode='a', header=False, index=False)
        QMessageBox.information(self, "GHI", "Ghi thành công")
class THU3(QMainWindow):
    def __init__(self):
        super(THU3, self).__init__()
        uic.loadUi('T3.ui', self)
        self.ql.clicked.connect(self.seg)
        self.ok.clicked.connect(self.OK)
        self.t2.clicked.connect(self.T2)
        self.t4.clicked.connect(self.T4)
        self.t5.clicked.connect(self.T5)
        self.t6.clicked.connect(self.T6)
        self.t7.clicked.connect(self.T7)
        self.cn.clicked.connect(self.CN)
    def seg(self):
        widget.setCurrentIndex(2)
    def T2(self):
        widget.setCurrentIndex(4)
    def T4(self):
        widget.setCurrentIndex(6)
    def T5(self):
        widget.setCurrentIndex(7)
    def T6(self):
        widget.setCurrentIndex(8)
    def T7(self):
        widget.setCurrentIndex(9)
    def CN(self):
        widget.setCurrentIndex(10)
    def OK(self):
        jod_input = self.jod.text().strip()
        status_input = self.do_2.text().strip()
        new_user = pd.DataFrame({'jod': [jod_input], 'do': [status_input]})
        new_user.to_csv('T3.csv', mode='a', header=False, index=False)
        QMessageBox.information(self, "GHI", "Ghi thành công")
class THU4(QMainWindow):
    def __init__(self):
        super(THU4, self).__init__()
        uic.loadUi('T4.ui', self)
        self.ql.clicked.connect(self.seg)
        self.ok.clicked.connect(self.OK)
        self.t3.clicked.connect(self.T3)
        self.t2.clicked.connect(self.T2)
        self.t5.clicked.connect(self.T5)
        self.t6.clicked.connect(self.T6)
        self.t7.clicked.connect(self.T7)
        self.cn.clicked.connect(self.CN)
    def seg(self):
        widget.setCurrentIndex(2)
    def T3(self):
        widget.setCurrentIndex(5)
    def T2(self):
        widget.setCurrentIndex(4)
    def T5(self):
        widget.setCurrentIndex(7)
    def T6(self):
        widget.setCurrentIndex(8)
    def T7(self):
        widget.setCurrentIndex(9)
    def CN(self):
        widget.setCurrentIndex(10)
    def OK(self):
        jod_input = self.jod.text().strip()
        status_input = self.do_2.text().strip()
        new_user = pd.DataFrame({'jod': [jod_input], 'do': [status_input]})
        new_user.to_csv('T4.csv', mode='a', header=False, index=False)
        QMessageBox.information(self, "GHI", "Ghi thành công")

class THU5(QMainWindow):
    def __init__(self):
        super(THU5, self).__init__()
        uic.loadUi('T5.ui', self)
        self.ql.clicked.connect(self.seg)
        self.ok.clicked.connect(self.OK)
        self.t3.clicked.connect(self.T3)
        self.t4.clicked.connect(self.T4)
        self.t2.clicked.connect(self.T2)
        self.t6.clicked.connect(self.T6)
        self.t7.clicked.connect(self.T7)
        self.cn.clicked.connect(self.CN)
    def seg(self):
        widget.setCurrentIndex(2)
    def T3(self):
        widget.setCurrentIndex(5)
    def T4(self):
        widget.setCurrentIndex(6)
    def T2(self):
        widget.setCurrentIndex(4)
    def T6(self):
        widget.setCurrentIndex(8)
    def T7(self):
        widget.setCurrentIndex(9)
    def CN(self):
        widget.setCurrentIndex(10)
    def OK(self):
        jod_input = self.jod.text().strip()
        status_input = self.do_2.text().strip()
        new_user = pd.DataFrame({'jod': [jod_input], 'do': [status_input]})
        new_user.to_csv('T5.csv', mode='a', header=False, index=False)
        QMessageBox.information(self, "GHI", "Ghi thành công")
class THU6(QMainWindow):
    def __init__(self):
        super(THU6, self).__init__()
        uic.loadUi('T6.ui', self)
        self.ql.clicked.connect(self.seg)
        self.ok.clicked.connect(self.OK)
        self.t3.clicked.connect(self.T3)
        self.t4.clicked.connect(self.T4)
        self.t5.clicked.connect(self.T5)
        self.t2.clicked.connect(self.T2)
        self.t7.clicked.connect(self.T7)
        self.cn.clicked.connect(self.CN)
    def seg(self):
        widget.setCurrentIndex(2)
    def T3(self):
        widget.setCurrentIndex(5)
    def T4(self):
        widget.setCurrentIndex(6)
    def T5(self):
        widget.setCurrentIndex(7)
    def T2(self):
        widget.setCurrentIndex(4)
    def T7(self):
        widget.setCurrentIndex(9)
    def CN(self):
        widget.setCurrentIndex(10)
    def OK(self):
        jod_input = self.jod.text().strip()
        status_input = self.do_2.text().strip()
        new_user = pd.DataFrame({'jod': [jod_input], 'do': [status_input]})
        new_user.to_csv('T6.csv', mode='a', header=False, index=False)
        QMessageBox.information(self, "GHI", "Ghi thành công")
class THU7(QMainWindow):
    def __init__(self):
        super(THU7, self).__init__()
        uic.loadUi('T7.ui', self)
        self.ql.clicked.connect(self.seg)
        self.ok.clicked.connect(self.OK)
        self.t3.clicked.connect(self.T3)
        self.t4.clicked.connect(self.T4)
        self.t5.clicked.connect(self.T5)
        self.t6.clicked.connect(self.T6)
        self.t2.clicked.connect(self.T2)
        self.cn.clicked.connect(self.CN)
    def seg(self):
        widget.setCurrentIndex(2)
    def T3(self):
        widget.setCurrentIndex(5)
    def T4(self):
        widget.setCurrentIndex(6)
    def T5(self):
        widget.setCurrentIndex(7)
    def T6(self):
        widget.setCurrentIndex(8)
    def T2(self):
        widget.setCurrentIndex(4)
    def CN(self):
        widget.setCurrentIndex(10)
    def OK(self):
        jod_input = self.jod.text().strip()
        status_input = self.do_2.text().strip()
        new_user = pd.DataFrame({'jod': [jod_input], 'do': [status_input]})
        new_user.to_csv('T7.csv', mode='a', header=False, index=False)
        QMessageBox.information(self, "GHI", "Ghi thành công")
class CN(QMainWindow):
    def __init__(self):
        super(CN, self).__init__()
        uic.loadUi('CN.ui', self)
        self.ql.clicked.connect(self.seg)
        self.ok.clicked.connect(self.OK)
        self.t3.clicked.connect(self.T3)
        self.t4.clicked.connect(self.T4)
        self.t5.clicked.connect(self.T5)
        self.t6.clicked.connect(self.T6)
        self.t7.clicked.connect(self.T7)
        self.t2.clicked.connect(self.T2)
    def seg(self):
        widget.setCurrentIndex(2)
    def T3(self):
        widget.setCurrentIndex(5)
    def T4(self):
        widget.setCurrentIndex(6)
    def T5(self):
        widget.setCurrentIndex(7)
    def T6(self):
        widget.setCurrentIndex(8)
    def T7(self):
        widget.setCurrentIndex(9)
    def T2(self):
        widget.setCurrentIndex(4)
    def OK(self):
        jod_input = self.jod.text().strip()
        status_input = self.do_2.text().strip()
        new_user = pd.DataFrame({'jod': [jod_input], 'do': [status_input]})
        new_user.to_csv('cn.csv', mode='a', header=False, index=False)
        QMessageBox.information(self, "GHI", "Ghi thành công")
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login_in = Login_in()
login_up = Login_up()
main1 = Main1()
main2 = Main2()
thu2 = THU2()
thu3 = THU3()
thu4 = THU4()
thu5 = THU5()
thu6 = THU6()
thu7 = THU7()
cn  = CN()
widget.addWidget(login_in)
widget.addWidget(login_up)
widget.addWidget(main1)
widget.addWidget(main2)
widget.addWidget(thu2)
widget.addWidget(thu3)
widget.addWidget(thu4)
widget.addWidget(thu5)
widget.addWidget(thu6)
widget.addWidget(thu7)
widget.addWidget(cn)
widget.setFixedHeight(620)
widget.setFixedWidth(950)
widget.setCurrentIndex(0)
widget.show()
app.exec()
