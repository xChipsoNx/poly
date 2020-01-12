import sqlite3
import user as u


class DBHelper:
    def __init__(self, dbname: object = "./sqlite3db.db") -> object:
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def new_user(self, name, phone, age):
        try:
            stmt = "INSERT OR IGNORE INTO Users(name, phone, age)VALUES(?,?, ?)"
            args = (name, phone, age) 
            self.conn.execute(stmt, args)
        except (sqlite3.OperationalError, sqlite3.ProgrammingError) as e:
            print("ERROR DATABASE new_user", e)
            self.conn.close()
        else:
            self.conn.commit()

    def get_userinfo(self, key):
        try:
            stmt = "SELECT * FROM Users WHERE Phone = (?)"
            args = (key,)
            self.conn.execute(stmt, args)

            for x in self.conn.execute(stmt, args):
                return u.User(x[0], x[1], x[2])

        except (sqlite3.OperationalError, sqlite3.ProgrammingError):
            print("ERROR DATABASE get_userinfo")
            self.conn.close()


    def get_all_phones(self):
        stmt = "SELECT phone FROM Users "
        cur = self.conn.cursor()
        phones = [phone[0] for phone in cur.execute(stmt)]
        return phones

    def get_all_amount_rating(self):
        stmt = "SELECT amountAll FROM Storage"
        cur = self.conn.cursor()
        amounts = [amount[0] for amount in cur.execute(stmt)]
        return amounts

    def get_classes_amount_rating(self, classes):
        stmt = "SELECT amountAll FROM Storage where classes = (?)"
        args = (classes, )
        cur = self.conn.cursor()
        amounts = [amount[0] for amount in cur.execute(stmt, args)]
        return amounts

    def get_amount_by_dates(self, name):
        stmt = "SELECT * FROM Buys where name = (?)"
        args = (name, )
        cur = self.conn.cursor()
        amounts = [amount[0] for amount in cur.execute(stmt, args)]
        return amounts

    def get_all_ages(self):
        stmt = "SELECT age FROM Users"
        cur = self.conn.cursor()
        ages = [age[0] for age in cur.execute(stmt)]
        return ages

    def get_critical(self):
        stmt = "SELECT name FROM Storage where have <= 3"
        cur = self.conn.cursor()
        return [x[0] for x in cur.execute(stmt)]

    def get_status(self):
        stmt = "SELECT name FROM Storage where status != NULL"
        cur = self.conn.cursor()
        return [x[0] for x in cur.execute(stmt)]

    def get_price(self, name):
        stmt = "SELECT price FROM Storage where name = (?)"
        args = (name, )
        cur = self.conn.execute(stmt, args)
        return cur.fetchone()[0]


