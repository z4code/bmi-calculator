# app.py

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bmi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database model.
class UserBMI(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	surname = db.Column(db.String(50), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.String(50), nullable=False)
	height = db.Column(db.Float, nullable=False)
	weight = db.Column(db.Float, nullable=False)
	bmi = db.Column(db.Float, nullable=False)
	category = db.Column(db.String(20), nullable=False)

# Initialize the database.
with app.app_context():
	db.create_all()
	print('SUCCESS!')

@app.route('/', methods=['GET', 'POST'])
def index():
	BMI = None
	category = None

	if request.method == 'POST':
		name = request.form['name']
		surname = request.form['surname']
		age = int(request.form['age'])
		gender = request.form['gender']
		height = float(request.form['height']) / 100
		weight = float(request.form['weight'])

		# Calculate BMI.
		BMI = round(weight / (height * height), 2)

		# Determine the category based on BMI.
		if BMI < 18.5:
			category = 'Underweight'
		elif 18.5 <= BMI < 24.5:
			category = 'Normal weight'
		elif 25 <= BMI < 29.9:
			category = 'Overweight'
		else:
			category = 'Obese'

		# Save to the database.
		new_BMI = UserBMI(name=name, surname=surname,
			age=age, gender=gender, height=height * 100, weight=weight,
			bmi=BMI, category=category)
		db.session.add(new_BMI)
		db.session.commit()

	return render_template('index.html', BMI=BMI, category=category)

if __name__ == '__main__':
	app.run(debug=True)