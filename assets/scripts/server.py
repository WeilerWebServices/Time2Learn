from flask import Flask, render_template, request, jsonify, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="time2learn_db",
        user="your_db_user",
        password="your_password"
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        session['user_id'] = user[0]
        return jsonify({'status': 'success'})
    return jsonify({'status': 'fail'})

@app.route('/lessons')
def lessons():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM lessons')
    lessons = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(lessons)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    # Logic to submit the quiz and track progress
    pass

if __name__ == '__main__':
    app.run(debug=True)
