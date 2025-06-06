import sqlite3
import bcrypt


class Connect():
    def __init__(self):
        pass
    def Session(self):
        pass
    def LogIn(self, login:str, pwd:str) -> bool:
        try:
            with sqlite3.connect('schedulerDB.db') as con :
                cursor = con.cursor()
                pwdfromdb = cursor.execute("Select PWD from Employees where login = ?", (login,)).fetchone()
                return self.check_password(pwd, pwdfromdb[0])
        except Exception as e:
            print('ERROR', e)

    def LogUp(self, fio:str, login:str, pwd:str):
        pwd = self.hash_password(pwd)
        try:
            with sqlite3.connect('schedulerDB.db') as con :
                cursor = con.cursor()
                cursor.execute("INSERT INTO Employees (FIO, login, PWD) VALUES (?,?,?)", (fio, login, pwd))
                con.commit()
        except Exception as e:
            print('ERROR', e)

    def hash_password(self, pwd:str)-> bytes:
        return bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
    def check_password(self, pwdfromuser:str, pwdfromdb:bytes )->bool:
            return bcrypt.checkpw(pwdfromuser.encode('utf-8'), pwdfromdb)


session1 = Connect()
#print(session1.LogIn('ivanov', 'Sa12VB_we'))
session1.LogUp('Администратор', 'sa', '123')