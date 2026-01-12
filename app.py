from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# تجهيز قاعدة البيانات
def init_db():
    conn = sqlite3.connect('medibyte.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS product_requests 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, org TEXT, qty TEXT, notes TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/request-product')
def request_page():
    return render_template('request.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_request', methods=['POST'])
def submit_request():
    name = request.form.get('name')
    email = request.form.get('email')
    org = request.form.get('org')
    qty = request.form.get('qty')
    notes = request.form.get('notes', '')

    conn = sqlite3.connect('medibyte.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product_requests (name, email, org, qty, notes) VALUES (?,?,?,?,?)", 
                   (name, email, org, qty, notes))
    conn.commit()
    conn.close()
    return render_template('success.html')

# السطر الأهم للتشغيل
if __name__ == '__main__':
    print("Server is launching...")
    app.run(debug=False, port=5000)