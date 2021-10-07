import os
import mysql.connector
class Login_page:
    def __init__(self, name=None, login=None, age=None, password=None):
        self.name = name
        self.login = login
        self.age = age
        self.password = password
        self.one_two = ["1", "2"]
        self.showfirst()

    def showfirst(self):
        print("""Welcome choose one of this
        1) Register
        2) Login
        Enter 1 or 2
        """)
        self.log_reg()

    def log_reg(self):
        to_know = input()
        while to_know not in self.one_two:
            os.system("cls")
            self.showfirst()
            to_know = input()
        if to_know == self.one_two[0]:
            self.register()
        else:
            self.loginn()

    def register(self):
        name = input("enter your name :").strip().capitalize()
        while not name:
            name = input("enter your name :").strip().capitalize()
        print("your name -->", name)
        login = input("enter your login :").strip()
        while not login or not self.istrue(login):
            login = input("enter your login :").strip()
        print("your name -->", name)
        print("your login -->", login)
        age = input("enter your age :").strip()
        while not age.isdigit():
            age = input("enter your age :").strip()
        age = int(age)
        print("your name -->", name)
        print("your login -->", login)
        print("your age -->", age)
        password = input("enter your password :").strip()
        while not password.isdigit():
            password = input("enter your password :").strip()
        password = int(password)
        print("your name -->", name)
        print("your login -->", login)
        print("your age -->", age)
        print("your password -->", password)
        self.write_sql(name, login, age, password)

    def loginn(self):
        print("yees")

    def istrue(self, login):
        istrue = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="login_page"
        )
        vazifa = istrue.cursor()
        true = vazifa.execute(f"select * from login where login = '{login}'")
        if true:
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






