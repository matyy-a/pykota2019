from django.db import models
from django.utils import timezone
from datetime import *


# Grupos

class groups (models.Model):
	groupname = models.CharField(max_length = 30)
	description = models.CharField(max_length = 50)
	limitby = models.CharField(
		max_length=20,
		choices=(('quota','quota'),),
		default='quota',
	)

	class Meta:
		managed = False
		db_table = 'groups'

	def __str__ (self):
		return '%s %s' % (self.groupname, self.description)

class groupsmembers (models.Model):
	groupid = models.ForeignKey('groups', on_delete=models.CASCADE, db_column='groupid')
	userid = models.ForeignKey('users', on_delete=models.CASCADE, db_column='userid')

	class Meta:
		managed = False
		db_table = 'groupsmembers'


	def __str__ (self):
		return '%s %s' % (self.groupid, self.userid,)

class printers (models.Model):
	printername = models.CharField('Nombre de la impresora', max_length = 30)
	description = models.CharField('Descripcion', max_length = 50)
	priceperpage = models.FloatField(default = 0.5)
	priceperjob = models.FloatField(default = 0)
	passthrough = models.CharField(
		max_length=20,
		choices=(('f','f'),),
		default='f',
	)
	maxjobsize = models.FloatField(default = 0)

	class Meta:
		managed = False
		db_table = 'printers'
	

	def __str__ (self):
		return '%s %s' % (self.printername, self.description)

class users (models.Model):
	username = models.CharField('Nombre de usuario', max_length=30)
	email= models.CharField(max_length=100)
	balance= models.FloatField(default = 0)
	lifetimepaid= models.FloatField(null = True)
	description= models.CharField('Descripcion', max_length=100)
	overcharge= models.FloatField(default = 1)
	level= models.CharField(max_length=15, null = True)

	class Meta:
		managed = False
		db_table = 'users'
	
	def __str__ (self):
		return '%s %s' % (self.username, self.description)

class userpquota (models.Model):
	userid = models.ForeignKey('users', on_delete=models.CASCADE, db_column='userid')    
	printerid= models.ForeignKey('printers', on_delete=models.CASCADE, db_column='printerid')
	lifepagecounter = models.IntegerField(default = 0)
	pagecounter= models.IntegerField(default = 0)
	softlimit= models.IntegerField('Limite blando', default = 0)
	hardlimit= models.IntegerField('Limite duro', default = 0)
	datelimit= models.DateTimeField(null=True)
	maxjobsize= models.IntegerField(null=True)
	warncount= models.IntegerField(default = 0)

	class Meta:
		managed = False
		db_table = 'userpquota'

	def __str__ (self):
		return '%s %s %s %s' % (self.userid, self.printerid, self.softlimit, self.hardlimit)