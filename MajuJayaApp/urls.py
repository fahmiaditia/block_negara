from django.urls import path, include
from django.contrib.auth import views
from .views import *


app_name = 'MajuJayaApp'

urlpatterns = [
	path('', index, name='index'),
	path('<uuidnya>/', page_inti, name='page_inti'),
]