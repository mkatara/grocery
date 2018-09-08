import sqlite3

class dbops:
    globalistid = 0
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
                  PURCHASEDFROM  TEXT,
                  ISLISTOPEN TEXT,
                  DATEOFPURCHASE TEXT DEFAULT CURRENT_DATE
                  ) """)
            except:
                pass

    def ins_row(self,veg1,listid):
                    self.c.execute("""insert into
                    grocery_list (listid,name,quantity,purchased,price,purchasedfrom,ISLISTOPEN)
                    values (?,?,?,?,?,?,?)""",(listid,veg1['NAME'],veg1['QUANTITY'], veg1['PURCHASED'], veg1['PRICE'], veg1['PURCHASEDFROM'],veg1['ISLISTOPEN']))
                    self.conn.commit()

    def fetch_row(self):#will add argument to accept a Date
                 self.c.execute("""select LISTID,NAME, QUANTITY, PURCHASED, PRICE,PURCHASEDFROM,DATEOFPURCHASE,ISLISTOPEN from GROCERY_LIST  order by listid desc""")
                 r = self.c.fetchall()
                 return r

    def gen_list_id(self):
                 self.c.execute(""" select ifnull(max(listid),1)+1 from grocery_list where listid is not null""")
                 return self.c.fetchone()[0]

    def closeList(self,lstid):
                 self.c.execute(""" update grocery_list set islistopen='N' where listid=? """,lstid)
                 self.conn.commit()
