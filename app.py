from flask import Flask, render_template, request, redirect, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # change this in production

# ---------- PostgreSQL Connection ----------
def get_db_connection():
    return psycopg2.connect(os.environ['DATABASE_URL'])

# ---------- Public Routes ----------
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
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO bookings (name, mobile, arrival, departure, persons, children, message)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', data)
    conn.commit()
    conn.close()
    return redirect('/')

# ---------- Admin Routes ----------
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
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM bookings ORDER BY id DESC')
    bookings = c.fetchall()
    conn.close()
    return render_template('admin.html', bookings=bookings)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')



# ---------- Run App ----------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

