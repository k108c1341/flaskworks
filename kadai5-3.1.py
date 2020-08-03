from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

datelist=[]
numlist=[]
n=0
average=0

def get_average(numlist):
    sum = 0
    for (x) in numlist:
        sum += x
    if len(numlist) == 0:
        return 0.0
    else:
        return sum / len(numlist)

@app.route('/')
def kadai5_3():
    return render_template('kadai5-3.html',n=n,average=average)

@app.route('/',methods=['POST'])
def send():
    num=request.form.get('num')
    if num != '':
        numlist.append(num)
        dt=datetime.datetime.now()
        dt=dt.strftime('%m/%d %H:%M')
        datelist.append(dt)
        n=int(len(numlist))
        average= get_average(numlist)

    return render_template('kadai5-3.html',numlist=numlist,datelist=datelist,n=n,average=average)

if __name__=='__main__':
    app.debug = True
    app.run()
