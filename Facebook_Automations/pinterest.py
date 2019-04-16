import requests
import json


class Constant():
    ACCESS_TOKEN = "**********************************8"
    AUTHORIZATION_URL = "https://api.pinterest.com/oauth/?response_type=code&client_id=5027576490951222399&redirect_uri=https://localhost:8000&scope=write_public read_public&state=mmldev_code"
    APP_ID=  "5027576490951222399"
    APP_SECRET = "***************"
    AUTHORIZE_URL = 'https://api.pinterest.com/oauth/'
    RETURN_URL = "https://localhost:8000"
    ACCESS_TOKEN_URL  = "https://api.pinterest.com/v1/oauth/token"
    BASE_URL = "https://api.pinterest.com/v1"
    CREATE_BOARD_ENDPOINT = "/boards/"
    CREATE_PINS_ENDPOINT = "/pins/"


def create_board(self, cmad):
	url =  Constant.BASE_URL+ Constant.CREATE_BOARD_ENDPOINT
	board_name = "Delhi Properties"
	data = {'name':board_name, 'description':"All properties postings from "+board_name,\
			'access_token':Constant.ACCESS_TOKEN}

	response =  requests.post(url, data=data)
	ar.write_social_media_api_calls("pinterest","create_board", "success", 1)
	result  = json.loads(response.text)
	locality_city = cmad.get_locality_name()+"_"+cmad.City
	print "Response :  ", response.text
	save_board_details(board_name , result['data']['id'], result['data']['url'], locality_city)
	return result['data']['name']



def create_pin(self, cmad):
	description = "This is test description"
	data = {'access_token': Constant.ACCESS_TOKEN, "board":"5235235345453534", "note":description}
	url =  Constant.BASE_URL+Constant.CREATE_PINS_ENDPOINT
	edited_image  =  open(edited_photo,'rb')
	files = {'image': edited_image}
	print "*************Calling create pin api****************"
	response = requests.post(url, files=files, data=data)
	result =  json.loads(response.text)
	print "Response: ", response.text
	return True, result['data']['url']


