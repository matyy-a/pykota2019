from django import forms
from .models import *

class groupsForm (forms.ModelForm):
	class Meta:
		model = groups
		fields = ('groupname', 'description',)

class groupsmembersForm (forms.ModelForm):
	class Meta:
		model = groupsmembers
		fields = ('userid', 'groupid',)

class printersForm (forms.ModelForm):

	class Meta:
		model = printers
		fields = ('printername', 'description',)

class usersForm(forms.ModelForm):
    class Meta:
   	 model= users
   	 fields= ('username', 'email', 'description')


class userpquotaForm(forms.ModelForm):
    class Meta:
   	 model= userpquota
   	 fields= ('userid', 'softlimit', 'hardlimit', 'printerid')