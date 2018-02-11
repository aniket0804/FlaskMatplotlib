from flask import Flask, render_template, redirect, request, session, abort, flash
import os

from model import InputForm
from compute import compute

from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///test.db', echo=True)

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('layout.html')


@app.route('/getchart', methods=['GET','POST'])
def getchart():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		form = InputForm(request.form)
		if request.method == 'POST' and form.validate():
			result = compute(form.Amplitude.data,form.Damping_Factor.data,form.Frequency.data,form.Time_Interval.data)
			print(result)
		else:
			result = None
			print("Nothing")
		return render_template('getchart.html', form=form, result=result)

@app.route('/home')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('home.html',msg="You're logged in",user=session.get('inputEmail'))


@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		POST_EMAILID = str(request.form['inputEmail'])
		POST_PASSWORD = str(request.form['inputPassword'])
		Session = sessionmaker(bind=engine)
		s = Session()
		query = s.query(User).filter(User.username.in_([POST_EMAILID]), User.password.in_([POST_PASSWORD]))
		result = query.first()
		if result:
			session['logged_in'] = True
			session['inputEmail'] = request.form['inputEmail'].split('@')[0]
			return redirect('/home')
		else:
			flash('wrong password!')
	return home()


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route("/logout")
def logout():
	session['logged_in'] = False
	return home()


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)
