import datetime
import sqlite3
import time
from dataclasses import dataclass


@dataclass
class Shift():
        date:str
        timestart:str
        timeend:str
        employee:str


class FuncShifts():
    def __init__(self):
        pass

    def AddShift(self, cur_user:str, shift: Shift)->None:
        try:
            if shift.date < datetime.date.today().isoformat():  #формат даты!!!!
                print(shift.date, datetime.date.today().isoformat()  )
                print('нельзя добавить смену датой раньше чем сегодня')
            else:
                with sqlite3.connect('schedulerDB.db') as con :
                    cursor = con.cursor()
                    id_emp = cursor.execute('SELECT ID FROM Employees where Login = ?', (shift.employee,)).fetchone()
                    id_emp = id_emp[0]

                    if self.check_conflict(shift.date, id_emp, shift.timestart, shift.timeend):
                        cursor.execute('INSERT INTO Shifts (IDEmployee, DateShift, TimeStart, TimeEnd, WhoCreated, WhenCreated) '
                                                      'VALUES (?,?,?,?,?,?)', (id_emp, shift.date, shift.timestart, shift.timeend,cur_user, datetime.datetime.now().isoformat() ) )
                        con.commit()
        except Exception as e:
            print(e)

    def UpdateShift(self):
        pass

    def DeleteShift(self):
        pass
    def check_conflict(self,  dateshift,  id_emp:str, timestart, timeend)->bool:
        with sqlite3.connect('schedulerDB.db') as con:
            cursor = con.cursor()
            dt_shift = cursor.execute('SELECT DateShift, TimeStart, TimeEnd FROM Shifts where IDEmployee = ? and DateShift = ? and TimeStart = ? and TimeEnd = ? ',
                                      (id_emp, dateshift, timestart, timeend )).fetchall()
            if len(dt_shift) > 0:
                return False
            else:
                return True




shift1 = Shift('2025-06-04', '12:00', '20:00', 'ivanov')
func = FuncShifts()
func.AddShift('sa', shift1)
