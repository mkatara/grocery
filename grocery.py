import sqlite3
from flask import Flask, render_template, request, url_for, redirect
from db import dbops

app = Flask(__name__)
app.config['SERVER_NAME']='127.0.0.1:5000'
dbc = dbops()
#vegetables = ['potato','tomato','onions','okara]
vegetableRow = list()
vegetableSet = list()

@app.route('/', methods=['GET','POST'])
def index():
    dbc.globalistid = dbc.gen_list_id()#to set a global listid value
    return render_template('dashboard.html')

@app.route('/CreateList.html',methods=['GET','POST'])
def createList():
    if request.method == 'POST':
        itemname=request.form['item']
        QUANTITY=request.form['QUANTITY']
        BASKETED=request.form['BASKETED']
        price=request.form['price']
        PURCHASEDFROM=request.form['PURCHASEDFROM']
        vegetableRow=[]
        vegetableRow.append(itemname)
        vegetableRow.append(QUANTITY)
        vegetableRow.append(BASKETED)
        vegetableRow.append(price)
        vegetableRow.append(PURCHASEDFROM)
        listid=dbc.globalistid
        vegetableSet.append(vegetableRow)
        veg=dict(NAME=itemname,QUANTITY=QUANTITY,PURCHASED=BASKETED,PRICE=price,PURCHASEDFROM=PURCHASEDFROM,ISLISTOPEN='Y')
        dbc.ins_row(veg,listid)

    return render_template('CreateList.html',listitems=vegetableSet)

@app.route('/showReport.html', methods=['GET','POST'])
def showReport():
    #if request.method=='GET':
        purchases=dbc.fetch_row()
        return render_template('showReport.html',itemset=purchases)

@app.route('/closeList/<lstid>')
def closeList(lstid):
    dbc.closeList(lstid)
    return redirect(url_for('showReport'))


if __name__=='__main__':
    app.run(debug=True)
