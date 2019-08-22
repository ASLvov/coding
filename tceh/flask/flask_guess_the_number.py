import os
from flask import Flask, request
import random
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators


app=Flask(__name__)
app.config.update(
	DEBUG=True,
	FLASK_RANDOM_SEED=os.environ['FLASK_RANDOM_SEED'],
	WTF_CSRF_ENABLED=False,
	NUM=0,
)

class MyForm(FlaskForm):
	number = IntegerField(label='number', validators=[
		validators.NumberRange(min=1, max=10)
	])

@app.route('/', methods=['GET'])
def generate_number():
	#print('Random SEED = {}'.format(app.config['FLASK_RANDOM_SEED']))
	app.config['NUM']=random.randint(1,10)
	#print('Загадано число {}'.format(app.config['NUM']))
	return ('Число загадано!',200)

@app.route('/guess', methods=['POST'])
def check_number():
	form=MyForm(request.form)
	#print(form.number.data)
	#print(app.config['NUM'])
	if form.validate():
		if form.number.data>app.config['NUM']:
			return ('<',200)
		elif form.number.data<app.config['NUM']:
			return ('>',200)
		else:
			return ('=',200)
	else:
		return ('Число должно быть от 1 до 10', 400)

if __name__=='__main__':
	random.seed(app.config['FLASK_RANDOM_SEED'])
	app.run()