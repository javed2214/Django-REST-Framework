from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.

URL = "http://127.0.0.1:8000"

def index(request):
	return render(request, 'index.html')

def get_token(request):
	url = f"{URL}/api/auth/"
	username = request.GET.get('username')
	password = request.GET.get('password')
	response =  requests.post(url, data = {'username': username, 'password': password})
	return response.json()


def get_data(request):
	url = f"{URL}/api/users_list"
	header = {'Authorization': f'Token {get_token(request)}'}
	response = requests.get(url, headers = header)
	return (response.json())


def viewdata(request):
	data = get_data(request)
	context = {'data': data}
	return render(request, 'data.html', context)