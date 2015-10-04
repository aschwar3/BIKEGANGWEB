from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

generated = 1234
users = {1111: 9999, 2222: 8888, 3333: 7777, 4444: 6666, 5555: 5555}
# Key = Bike Share User ID, Value = Last 4 Digits of B Number
freeman = [1,2,3,4,5,6,7,8,9,10]
cpo = [11,12,13,14,15,16,17,18,19,20]

@app.route('/firstPage', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['machinecode']):
            return render_template('check.html')
        else:
            error = 'Invalid code'
    return render_template('firstPage.html', error=error)
    
@app.route('/out', methods=['POST', 'GET'])
def check_out():
    error = None
    if request.method == 'POST':
        userid = request.form['userid']
        pin = request.form['pin']
        if valid_id(userid,pin):
            return render_template('keys.html')
        else:
            error = 'Invalid entry'
    return render_template('out.html', error=error)
    
@app.route('/in', methods=['POST', 'GET'])
def check_in():
    error = None
    if request.method == 'POST':
        if valid_id(request.form['userid'],request.form['pin']):
            return render_template('keyreturn.html')
        else:
            error = 'Invalid entry'
    return render_template('in.html', error=error)
    
@app.route('/keys', methods=['POST', 'GET'])
def select_key():
    error = None
    if request.method == 'POST':
        response = request.form['keynum']
        if valid_key(response):
            if int(response) in freeman:
                freeman.remove(int(response))
            elif int(response) in cpo:
                cpo.remove(int(response))
            return render_template('firstPage.html')
        else:
            error = 'Invalid entry'
    return render_template('keys.html', error=error)
    
@app.route('/keyreturn', methods=['POST', 'GET'])
def return_key():
    error = None
    if request.method == 'POST':
        response = request.form['keynum']
        if valid_returnkey(response):
            if int(response)<11:
                freeman.append(int(response))
            else:
                cpo.append(int(response))
            return render_template('firstPage.html')
        else:
            error = 'Invalid entry'
    return render_template('keyreturn.html', error=error)
    
@app.route('/statusPage')
def load_status():
    return render_template('statusPage.html')
    
def valid_login(machinecode):
    return int(machinecode) == generated
    
def valid_id(userid,pin):
    return (int(userid) in users) and (users[int(userid)]==int(pin))
    
def valid_key(keynum):
    return (int(keynum) in freeman) or (int(keynum) in cpo)
    
def valid_returnkey(keynum):
    return True
    #return (int(keynum) not in freeman) and (int(keynum) not in cpo) and (int(keynum)<21)
    
if __name__ == '__main__':
    app.run()