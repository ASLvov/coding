# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms_alchemy import ModelForm
from models import Item

class ItemForm(ModelForm):
	class Meta:
		model = Item
