# -*- coding: utf-8 -*-
'''
ЗАДАНИЕ
Делаем анонимный блог (имиджборду)
Пользователь может написать пост: с заголовком и
содержанием
Пользователи могут оставлять комментарии под
записью
Пользователи отправляют POST запросы к серверу,
чтобы оставлять записи и комментарии
Необходимо использовать текстовые шаблоны для
вывода блога
'''
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db= SQLAlchemy(app)

@app.route('/', methods=['GET'])
def output():
	from models import Article, Comment
	from forms import ArticleForm, CommentForm
	articles = Article.query.all()
	comments = Comment.query.all()

	return render_template('all_articles.html', articles=articles)


@app.route('/create_article/', methods=['GET','POST'])
def input_article():
	from models import Article, Comment
	from forms import ArticleForm, CommentForm
	if request.method=='POST':
		print(request.form)
		form = ArticleForm(request.form)
		if form.validate():
			article = Article(**form.data)
			db.session.add(article)
			db.session.commit()
		return redirect("http://127.0.0.1:5000/")
	return render_template('create_article.html')


# @app.route('/create_comment', methods=['POST'])
# def input_comment():
# 	from models import Article, Comment
# 	from forms import ArticleForm, CommentForm
# 	if request.method=='POST':
# 		print(request.form)
# 		form = CommentForm(request.form)
# 		print(form.data)
# 		if form.validate():
# 			comment = Comment(**form.data)
# 			db.session.add(comment)
# 			db.session.commit()
# 			return 'Comment created!'

@app.route('/article/<id_number>', methods=['GET', 'POST'])
def show_article(id_number):
	from models import Article, Comment
	from forms import ArticleForm, CommentForm
	if request.method=='POST':
		print(request.form)
		form = CommentForm(request.form)
		form.article_id.data = int(id_number)
		print(form.data)
		if form.validate():
			comment = Comment(**form.data)
			db.session.add(comment)
			db.session.commit()
	articles = Article.query.filter_by(id = id_number)
	comments = Comment.query.filter_by(article_id = id_number)
	return render_template('some_article.html', articles=articles, comments=comments)

if __name__=='__main__':
	from models import *
	db.create_all()
	app.run()