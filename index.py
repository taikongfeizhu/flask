__author__ = 'jenking'

from flask import Flask, render_template, session, redirect, url_for, flash, make_response

from flask.ext.script import Manager
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

from wtforms import StringField, SubmitField
from wtforms.validators import Required
from wtforms.validators import DataRequired

from datetime import datetime
import os
import time
import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

moment = Moment(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
manager = Manager(app)


def trace(msg):
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    print "["+now+"]",msg

class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    username = db.Column(db.String(64), unique=True,index=True)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/data')
def database():

    return render_template('data.html')


@app.route('/moment')
def moment():
    return render_template('moment.html', mylist=["one", "two", "three", "four", "five"], current_time=datetime.utcnow())


@app.route('/usr/<name>')
def user(name):
    return render_template('user.html', name=name, user='wong')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
