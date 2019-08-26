# -*- coding: utf-8 -*-
import datetime
from app import db

class Article(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	title = db.Column(db.String(80), unique = True, nullable = False)
	body = db.Column(db.String(500), nullable = False)
	datetime = db.Column(db.DateTime, default = datetime.datetime.now())
	is_visible = db.Column(db.Integer, default=1, nullable=False)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	
	article_id = db.Column(
		db.Integer, 
		db.ForeignKey('article.id'), 
		nullable = False, 
		index = True
	)
	
	article = db.relationship(Article, foreign_keys=[article_id, ])

	text = db.Column(db.String(100), nullable = False)
	datetime = db.Column(db.DateTime, default = datetime.datetime.now())
