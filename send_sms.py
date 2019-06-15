from twilio.rest import Client
import json

data = json.load(open("output.json"))

def check_phone_number(phone_number):
	"""
		params: phone_number(type: text)

		return: phone number with format not included 0 firts in phone number
	"""
	phone = ""
	if phone_number[0] is '0':
        phone = phone_number[1:]
    elif phone_number[0] is '+':
        phone = phone_number[3:]
    else:
        phone = phone_number
    
    return phone

def send_sms(user, account_sid, auth_token):
	"""
		params: 
				user(type:dict): dictionary included infomation of user
				account_sid(type:str) : acc sid in twilio
				auth_token(type:str): token in twilio

		return: auto send sms to user  
	"""

	client = Client(account_sid, auth_token)
	phone = check_phone_number(user["mobile"])
	name = user["contactName"]
	type_ = user["type"]
	# area = user["area"]

	message = client.message.create(
					from_ = "",
					body = "push content of message",
					to = "84" + phone
		)

	




