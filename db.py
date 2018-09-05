import sqlite3

class dbops:

    def __init__(self):
            ##global c
            self.conn = sqlite3.connect('shopping.db', check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
            self.c = self.conn.cursor()
            try:
                self.c.execute("""CREATE TABLE GROCERY_LIST(
                  LISTID INTEGER,
                  NAME TEXT,
                  QUANTITY FLOAT,
                  PURCHASED TEXT,
                  PRICE TEXT,
                  ISLISTOPEN TEXT,
                  DATEOFPURCHASE TEXT DEFAULT CURRENT_DATE
                  ) """)
            except:
                pass

    def ins_row(self,veg1):
                    self.c.execute("""insert into
                    grocery_list (name,quantity,purchased,price,ISLISTOPEN)
                    values (?,?,?,?,?)""",(veg1['NAME'],veg1['QUANTITY'], veg1['PURCHASED'], veg1['PRICE'], veg1['ISLISTOPEN']))
                    self.conn.commit()

    def fetch_row(self):#will add argument to accept a Date
                 self.c.execute("""select NAME, QUANTITY, PURCHASED, PRICE, ISLISTOPEN,DATEOFPURCHASE from GROCERY_LIST """)
                 r = self.c.fetchall()
                 return r
