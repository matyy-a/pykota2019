from django.contrib import admin
from .models import *

admin.site.register(groups)
admin.site.register(groupsmembers)
admin.site.register(printers)
admin.site.register(users)
admin.site.register(userpquota)

