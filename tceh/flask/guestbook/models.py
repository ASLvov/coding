# -*- coding: utf-8 -*-
import datetime
from app import db

class Item(db.Model):
	item_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	item_author = db.Column(db.String(20), nullable = False)
	item_data = db.Column(db.String(80), nullable = False)
	item_datetime = db.Column(db.DateTime, default = datetime.datetime.now())
	is_visible = db.Column(db.Integer, default=1, nullable=False)

	def __str__(self):
		return '<Item with id %s created by %r>'.format(self.item_id, self.item_author)

	def to_json(self):
		return {
			'item_id':self.item_id,
			'item_author':self.item_author,
			'item_data':self.item_data,
			'item_datetime':self.item_datetime,
			'is_visible':self.is_visible
		}
