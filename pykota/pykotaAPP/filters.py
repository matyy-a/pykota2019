import django_filters
from .models import *

class userpquotaFilter (django_filters.FilterSet):
	class Meta:
		model = userpquota
		fields = ['printerid']