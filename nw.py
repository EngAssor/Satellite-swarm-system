from flask import Flask, render_template


app = Flask(__name__)
@app.route('/Telemtry Data')
def tl():
    return 'this is'

@app.route('/')
def index():
    with open('newnew.jpg', 'rb') as tr:
        cons = tr.read()
    return cons
@app.route('/telemetry' , methods=['GET','POST','PUT'])
def telemetry():
    with open('Telemetry.txt','r') as te:
        tel = te.read()
    return tel




if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.4',port=2560)
