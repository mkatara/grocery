import sqlite3
from flask import Flask, render_template, request
from db import dbops

app = Flask(__name__)
dbc = dbops()
#vegetables = ['potato','tomato','onions','okara]
vegetableRow = list()
vegetableSet = list()

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('dashboard.html')

@app.route('/CreateList.html',methods=['GET','POST'])
def createList():
    global vegetables
    if request.method == 'POST':
        x=request.form['item']
        QUANTITY=request.form['QUANTITY']
        BASKETED=request.form['BASKETED']
        price=request.form['price']
        PURCHASEDFROM=request.form['PURCHASEDFROM']
        vegetableRow.append(x)
        vegetableRow.append(QUANTITY)
        vegetableRow.append(BASKETED)
        vegetableRow.append(price)
        vegetableRow.append(PURCHASEDFROM)

        vegetableSet.append(vegetableRow)
        veg=dict(NAME=x,QUANTITY='QUANTITY',PURCHASED=BASKETED,PRICE=price,PURCHASEDFROM=PURCHASEDFROM,ISLISTOPEN='Y')
        dbc.ins_row(veg)
    return render_template('CreateList.html',listitems=vegetableSet)

@app.route('/showReport.html', methods=['GET','POST'])
def showReport():
    if request.method=='GET':
        #call db to get rows
        purchases=dbc.fetch_row()
        #purchases=dict([('grapes','29-08-2018'),('apples','29-08-2018')])
        #for r in purchases:
        return render_template('showReport.html',itemset=purchases)


if __name__=='__main__':
    app.run(debug=True)
