import requests
import json

URL = "http://127.0.0.1:8000"

# Get Auth Token
# Username & Password: javed
def get_token():
	url = f"{URL}/api/auth/"
	username = input("Enter UserName: ")
	password = input("Enter Password: ")
	response =  requests.post(url, data = {'username': username, 'password': password})
	return response.json()


def get_data():
	url = f"{URL}/api/users_list/"
	header = {'Authorization': f'Token {get_token()}'}
	response = requests.get(url, headers = header)
	print(response.json())


def create_new(id):
	url = f"{URL}/api/users_list/"
	header = {'Authorization': f'Token {get_token()}'}
	data = {
		"employee_id": f"HQ00{id}",
		"name": "Rowan Atkinson",
		"ranking": 7.2,
		"age": 65
	}
	response = requests.post(url, data = data, headers = header)


def edit_data(employee_id):
	url = f"{URL}/api/users_list/{employee_id}/"
	header = {'Authorization': f'Token {get_token()}'}
	data = {
		"name": "Mike Tyson"
	}
	response = requests.put(url, data = data, headers = header)
	print(response.text)


# get_data()	// To List out all the Data

# for x in range(30):	// To create new entries
	# create_new(x)

# edit_data(2)		// To modify the data using employee id