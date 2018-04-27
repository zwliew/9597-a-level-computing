import flask
import db

app = flask.Flask(__name__)
db.create()

@app.route('/')
def index():
    return flask.redirect(flask.url_for('get_questions'))

@app.route('/questions')
def get_questions():
    questions = db.get_questions()
    return flask.render_template('questions.html', questions=questions)

@app.route('/questions', methods=['post'])
def post_question():
    text = flask.request.form['text']
    answer = flask.request.form['answer']
    rowid = db.add_question(text, answer)
    return flask.redirect(flask.url_for('get_question', rowid=rowid))

@app.route('/questions/<int:rowid>')
def get_question(rowid):
    question = db.get_question(rowid)
    return flask.render_template('question.html', question=question, rowid=rowid)

@app.route('/questions/<int:rowid>', methods=['delete'])
def delete_question(id):
    db.delete_question(id)
    return flask.redirect(flask.url_for('get_questions'))

