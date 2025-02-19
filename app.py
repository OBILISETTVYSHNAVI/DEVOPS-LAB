from flask import Flask, render_template_string, request, send_from_directory
import os
app = Flask(__name__)
@app.route('/')
def registration():
    with open('Registration.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return render_template_string(html_content)
@app.route('/Registration.css')
def serve_css():
    return send_from_directory(os.getcwd(), 'Registration.css')
@app.route('/Registration.js')
def serve_js():
    return send_from_directory(os.getcwd(), 'Registration.js')
@app.route('/Registartion.js')
def serve_js_alias():
    return send_from_directory(os.getcwd(), 'Registration.js')
@app.route('/welcome')
def welcome():
    username = request.args.get('username', 'User')
    with open('Welcome.html', 'r', encoding='utf-8') as file:
        welcome_html = file.read()
    return render_template_string(welcome_html, username=username)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)