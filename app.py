from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/setcookie', methods=['POST'])
def setcookie():
    name = request.form['name']
    email = request.form['email']
    resp = make_response(redirect('/welcome'))
    resp.set_cookie('name', name)
    resp.set_cookie('email', email)
    return resp

@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    if not name:
        return redirect('/')
    return render_template('welcome.html', name=name)

@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('email', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
