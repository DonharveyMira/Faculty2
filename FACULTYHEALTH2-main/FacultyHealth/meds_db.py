#meds database
import sqlite3


class Meds_Database:
    def __init__(self, meds_db):
        self.con = sqlite3.connect(meds_db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS meds(
            id Integer Primary Key,
            code,
            description,
            name,
            quantity
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insertMeds(self, code, description, name, quantity):
        self.cur.execute("insert into meds values (NULL,?,?,?,?)",
                         (code, description, name, quantity))
        self.con.commit()

    # Fetch All Data from DB
    def fetchMeds(self):
        self.cur.execute("SELECT * from meds")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def removeMeds(self, id):
        self.cur.execute("DELETE from meds where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def updateMeds(self, id, code, description, name, quantity):
        self.cur.execute(
            "UPDATE meds set code=?, description=?, name=?, quantity=? where id=?",
            (code, description, name, quantity, id))
        self.con.commit()
