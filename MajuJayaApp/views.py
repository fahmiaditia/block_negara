from django.shortcuts import render
from .models import *
# Create your views here.


# MENDAPATKAN IP NEGARA #############
import json
from urllib.request import urlopen

sumber = "https://geolocation-db.com/json"
response = urlopen(sumber)
data_json = json.load(response)
#####################################



def index(request):
	negara = Data_Negara.objects.all()

	negara_sekarang = data_json['country_name']
	IP_negara = data_json['IPv4']

	context = {
		'negara': negara,
		'negara_ip': negara_sekarang,
		'ip': IP_negara,
	}
	return render(request, 'index.html', context)

def page_inti(request, uuidnya):
	negar = Data_Negara.objects.get(uuid_negara=uuidnya)

	negara_sekarang = data_json['country_name']
	IP_negara = data_json['IPv4']


	context = {
		'negara': negar,
		'negara_ip': negara_sekarang,
		'ip': IP_negara,
		'data_json': data_json,
	}
	return render(request, 'page_inti.html', context)