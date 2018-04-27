from flask import Flask, render_template, url_for, redirect, request, \
                    send_from_directory
from werkzeug import secure_filename
import os.path
import sqlite3

ALLOWED_EXTENSIONS = set(['bmp', 'gif', 'jpg', 'jpeg', 'png'])
UPLOAD_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'static/images'
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_db():
    db = sqlite3.connect('db.sqlite3')
    print('Opened database.')
    db.row_factory = sqlite3.Row
    return db

def create_db():
    db = get_db()
    db.execute('CREATE TABLE posting' \
                '(id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                'username TEXT,' \
                'email TEXT,' \
                'message TEXT)')
    print('Table created.')
    db.close()

if not os.path.isfile('db.sqlite3'):
    create_db()

@app.route('/form')
def get_form():
    return render_template('form.html')

@app.route('/form', methods=['post'])
def post_form():
    db = get_db()
    db.execute('INSERT INTO posting (username, email, message) VALUES (?,?,?)',
                (request.form['username'],
                request.form['email'],
                request.form['message']))
    db.commit()
    db.close()
    return redirect(url_for('success'))

@app.route('/update', methods=['get', 'post'])
def update():
    if request.method == 'post':
        db = get_db()
        db.execute('UPDATE posting WHERE id = ? SET message = ?',
                request.form['id'], request.form['message'])
        db.commit()
        db.close()
        return redirect(url_for('success'))
    else:
        db = get_db()
        records = db.execute('SELECT * FROM posting').fetchall()
        db.close()
        return render_template('update.html', records=records)
@app.route('/success')
def success():
    db = get_db()
    records = db.execute('SELECT * FROM posting').fetchall()
    db.close()
    return render_template('messageboard.html', records=records)

@app.route('/')
def index():
    return render_template('index.html', title='Index')

@app.route('/<int:age>/<name>')
def user(age, name):
    return render_template('user.html', title='User', age=age, name=name)

@app.route('/student')
def student():
    return redirect('teacher')

@app.route('/teacher')
def teacher():
    return 'Teacher'

@app.route('/display/<role>')
def display(role):
    if role == 'student' or role == 'teacher':
        return url_for(role)

@app.route('/oldform', methods = ['post'])
def form():
    return render_template('formresult.html',
                            name=request.form['name'],
                            email=request.form['email'],
                            message=request.form['message'])

@app.route('/upload')
def upload():
    return render_template('upload.html', title='Upload')

@app.route('/upload', methods = ['post'])
def process_upload():
    picture = request.files['picture']
    if picture.filename != '':
        if picture.filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            file = secure_filename(picture.filename)
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], file))
            return redirect(url_for('display_file', filename=picture.filename))
        return 'Failed to upload because file is not an image.'
    return 'Nothing was uploaded.'

@app.route('/file/<filename>')
def display_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
