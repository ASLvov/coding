# -*- coding: utf-8 -*-
'''
ЗАДАНИЕ
Реализовать гостевую книгу на Flask
1. Она должна содержать модель: 'Item' со следующими полями:
	1.1 Поле автор: любое значение
	1.2 Текст сообщения: может быть любой текст длиннее 5 символов
	1.3 Дата и время публикации
	1.4 Булевое поле: удалено или нет
2. Должна быть возможность получить все записи по адресу '/'
3. Должна быть возможность добавить запись по адресу '/create'
	3.1 Должна работать валидация при помощи формы модели
'''
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import config
import json

app = Flask(__name__)
app.config.from_object(config)

db= SQLAlchemy(app)

@app.route('/', methods=['GET'])
def output():
	from models import Item
	from forms import ItemForm
	items = Item.query.filter_by(is_visible=1)
	return jsonify([item.to_json() for item in items])

@app.route('/create', methods=['POST'])
def input_item():
	from models import Item
	from forms import ItemForm
	if request.method=='POST':
		print(request.form)
		form = ItemForm(request.form)
		if form.validate():
			item = Item(**form.data)
			db.session.add(item)
			db.session.commit()
			return 'Item created!'
	
if __name__=='__main__':
	from models import *
	db.create_all()
	app.run()