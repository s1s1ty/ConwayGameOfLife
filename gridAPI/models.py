# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Grid(models.Model):
	x = models.IntegerField(default=0)
	y = models.IntegerField(default=0)
	data = models.TextField()

	def __str__(self):
		return str(data)
		
