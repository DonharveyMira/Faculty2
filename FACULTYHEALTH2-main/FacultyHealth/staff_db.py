import sqlite3

class Staff_Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql= """
        CREATE TABLE IF NOT EXISTS staff(
            id Integer Primary Key,
            name text,
            contact text,
            address text,
            sex text,
            user text,
            password text
        )
        """

        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, contact, address, sex, user, password):
        self.cur.execute("insert into staff values (NULL,?,?,?,?,?,?)",
                         (name, contact, address, sex, user, password))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from staff")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("DELETE from staff where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, contact, address, sex, user, password):
        self.cur.execute(
            "UPDATE staff set name=?,contact=?, address=?, sex=?, user=?, password=? where id=?",
            (name, contact, address, sex, user, password, id))
        self.con.commit()
