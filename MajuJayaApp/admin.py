from django.contrib import admin
from .models import *

# Register your models here.

class Data_Negara_Admin(admin.ModelAdmin):
	list_display=(
		'nama_negara', 'uuid_negara'
	)
	readonly_fields = ['uuid_negara']

admin.site.register(Data_Negara, Data_Negara_Admin)