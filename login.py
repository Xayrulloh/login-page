import os
import mysql.connector
class Login_page:
    def __init__(self):
        self.login = ""
        self.one_two_three = ["1", "2", "3"]
        self.one_two = ["1", "2"]
        self.log_reg()

    def showfirst(self):
        print("""Welcome choose one of this
        1) Register
        2) Login
        Enter 1 or 2
        """)
    def log_reg(self):
        self.showfirst()
        to_know = input("enter")
        while to_know not in self.one_two:
            os.system("cls")
            self.showfirst()
            to_know = input("enter")
        if to_know == self.one_two[0]:
            self.register()
        else:
            self.loginn()

    def register(self):
        name = input("enter your name :").strip().capitalize()
        while not name:
            os.system("cls")
            name = input("enter your name :").strip().capitalize()
        print("your name -->", name)
        login = input("enter your login :").strip()
        while not login or not self.istrue(login):
            os.system("cls")
            login = input("enter your login :").strip()
        print("your name -->", name)
        print("your login -->", login)
        age = input("enter your age :").strip()
        while not age.isdigit():
            os.system("cls")
            age = input("enter your age :").strip()
        age = int(age)
        print("your name -->", name)
        print("your login -->", login)
        print("your age -->", age)
        password = input("enter your password :").strip()
        while not password.isdigit():
            os.system("cls")
            password = input("enter your password :").strip()
        password = int(password)
        print("your name -->", name)
        print("your login -->", login)
        print("your age -->", age)
        print("your password -->", password)
        self.write_sql(name, login, age, password)

    def loginn(self):
        login = input("enter your login :").strip()
        while not self.isfalse(login):
            os.system("cls")
            login = input("enter your login :").strip()
        self.login = login
        password = input("enter your password :").strip()
        while not self.passw(password):
            os.system("cls")
            password = input("enter your password :").strip()
        self.changes()

    def showsecond(self):
        print("""Choose on of this
            1) change login/password
            2) log out
            3) delete account
        """)

    def changes(self):
        self.showsecond()
        num = input("enter")
        while num not in self.one_two_three:
            os.system("cls")
            self.showsecond()
            num = input("enter")
        if num == self.one_two_three[0]:
            self.change_log_passw()
        elif num == self.one_two_three[1]:
            self.log_out()
        elif num == self.one_two_three[2]:
            self.del_acc(self.login)

    def change_log_passw(self):
        self.over()

    def show_third(self):
        print("""Choose on of them :
            1) change login
            2) change password
            3) change login and password
        """)

    def over(self):
        self.show_third()
        num = input("enter")
        if num == self.one_two_three[0]:
            self.change_login()
        elif num == self.one_two_three[1]:
            self.change_password()
        elif num == self.one_two_three[2]:
            self.change_login_password()

    def change_login(self):
        new_login = input("Enter new login :").strip()
        while not new_login:
            os.system("cls")
            new_login = input("Enter new login :").strip()
        change = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="login_page"
        )
        project = change.cursor()
        project.execute(f"update login set login='{new_login}' where login='{self.login}'")
        change.commit()

    def change_password(self):
        new_password = input("Enter new password :").strip()
        while not new_password.isdigit():
            os.system("cls")
            new_password = input("Enter new password :").strip()
        new_password = int(new_password)
        change = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="login_page"
        )
        project = change.cursor()
        project.execute(f"update login set password='{new_password}' where login='{self.login}'")
        change.commit()
    def change_login_password(self):
        self.change_password()
        self.change_login()
    def log_out(self):
        self.log_reg()

    def del_acc(self, login):
        delet = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="login_page"
        )
        project = delet.cursor()
        project.execute(f"delete from login where login ='{login}'")
        delet.commit()


    def passw(self, password):
        to_str = self.result[0][4]
        to_str = str(to_str)
        if password == to_str:
            return True
        return False

    def isfalse(self, login):
        isfalse = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="login_page"
        )
        vazifa = isfalse.cursor()
        false = f"select * from login where login ='{login}'"
        vazifa.execute(false)
        result = vazifa.fetchall()
        self.result = result
        if result:
            return True
        return False

    def istrue(self, login):
        istrue = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="login_page"
        )
        vazifa = istrue.cursor()
        true = f"select * from login where login = '{login}'"
        vazifa.execute(true)
        result = vazifa.fetchall()
        if result:
            return False
        return True

    def write_sql(self, name, login, age, password):
        reg = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="login_page"
        )
        project = reg.cursor()
        project.execute(f"insert into login(name, login, age, password) values('{name}', '{login}', '{age}', '{password}')")
        reg.commit()


Xayulloh = Login_page()






