# from flask import Flask, render_template, request, redirect, session
# import sqlite3

# app = Flask(__name__)
# app.secret_key = 'secret'

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         conn = get_db_connection()
#         user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password)).fetchone()
#         conn.close()
#         if user:
#             session['user'] = user['username']
#             return redirect('/dashboard')
#         else:
#             return "Login failed"
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         conn = get_db_connection()
#         conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
#         conn.commit()
#         conn.close()
#         return redirect('/login')
#     return render_template('signup.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'user' not in session:
#         return redirect('/login')
#     return render_template('dashboard.html', user=session['user'])

# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect('/login')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('login.html')  # or 'index.html' if it exists

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # ✅ Home Route (important for deployment)
# @app.route('/')
# def home():
#     return render_template('login.html')

# # ✅ Your existing routes (example)
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # your login logic here
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     # your signup logic here
#     return render_template('signup.html')

# @app.route('/dashboard')
# def dashboard():
#     # your dashboard logic here
#     return render_template('dashboard.html')

# # ✅ Run only for local testing; not used on Render
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# ✅ New root route for deployment (important!)
@app.route('/')
def home():
    return render_template('login.html')  # Or redirect to /login if preferred

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE email = ? AND password = ?', 
            (email, password)
        ).fetchone()
        conn.close()
        if user:
            session['user'] = user['username']
            return redirect('/dashboard')
        else:
            return "Login failed"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (username, email, password)
        )
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# ✅ Remove this line when deploying with gunicorn (keep it only for local)
if __name__ == '__main__':
    app.run(debug=True)

