from flask import Flask, render_template, request, redirect
import mysql.connector as db
import os
import json

db_param = {
    'user' : 'mysql',
    'host' : 'localhost',
    'password' : '',
    'database' : 'itemdb'
}

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = './static/uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM list'
    cur.execute(stmt)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', list=rows)

@app.route('/send', methods=['POST'])
def send():
    title = request.form.get('title')
    price = request.form.get('price')
    if title=="" or price=="":
        return redirect('/')
    conn = db.connect(**db_param)
    cur = conn.cursor()

    stmt = 'SELECT * FROM books WHERE title=%s'
    cur.execute(stmt, (title,))
    rows = cur.fetchall()
    if len(rows)==0:
        cur.execute('INSERT INTO books(title, price) VALUES(%s, %s)', (title, int(price)))
    else:
        cur.execute('UPDATE books SET price=%s WHERE title=%s', (int(price), title))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    del_list = request.form.getlist('del_list')
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'DELETE FROM books WHERE id=%s'
    for id in del_list:
        cur.execute(stmt, (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

if __name__=='__main__':
    app.debug = True
    app.run()