from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def kadai5_1():
    return render_template('kadai5-1.html')

@app.route('/send', methods=['POST'])
def send():
    msg1 = request.form.get('msg1')
    msg2 = request.form.get('msg2')
    return render_template('receive5-1.html', message1=msg1, message2=msg2)
if __name__=='__main__':
    app.debug = True
    app.run()