from flask import Flask, render_template, request, redirect
import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('tours.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        arrival TEXT,
        departure TEXT,
        persons INTEGER,
        children INTEGER,
        message TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = (
        request.form['name'],
        request.form['mobile'],
        request.form['arrival'],
        request.form['departure'],
        request.form['persons'],
        request.form['children'],
        request.form['message']
    )
    conn = sqlite3.connect('tours.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO bookings (name, mobile, arrival, departure, persons, children, message)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()
    return redirect('/')

from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # use a strong one in production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = (
        request.form['name'],
        request.form['mobile'],
        request.form['arrival'],
        request.form['departure'],
        request.form['persons'],
        request.form['children'],
        request.form['message']
    )
    conn = sqlite3.connect('tours.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO bookings (name, mobile, arrival, departure, persons, children, message)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()
    return redirect('/')

# ---------- Admin Area ----------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['admin'] = True
            return redirect('/admin')
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/admin')
def admin():
    if not session.get('admin'):
        return redirect('/login')
    conn = sqlite3.connect('tours.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bookings ORDER BY id DESC')
    bookings = c.fetchall()
    conn.close()
    return render_template('admin.html', bookings=bookings)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)

with open(os.path.join(base_dir, "app.py"), "w") as f:
    f.write(app_py)

with open(os.path.join(template_dir, "home.html"), "w") as f:
    f.write(home_html)

with open(os.path.join(template_dir, "about.html"), "w") as f:
    f.write(about_html)

with open(os.path.join(template_dir, "contact.html"), "w") as f:
    f.write(contact_html)

with open(os.path.join(static_dir, "style.css"), "w") as f:
    f.write(style_css)

shutil.make_archive(base_dir, 'zip', base_dir)
"/mnt/data/simple_travel_site.zip"
