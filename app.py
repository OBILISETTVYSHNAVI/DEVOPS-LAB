from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder=os.getcwd())

@app.route('/')
def index():
    return render_template('Registration.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        gender = request.form['gender']
        print(f"Full Name: {full_name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Password: {password}")
        print(f"Gender: {gender}")
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
