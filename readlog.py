# TDA4vm Edge Impulse bag detector log reader and alert
# Roni Bandini @RoniBandini
# Usage python3 readlog.py

import requests

def telegramAlert(message):

	apiToken = '00:000'
	chatID = '-0000'
	apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

	try:
		response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
		print(response.text)
	except Exception as e:
		print(e)

myLimit=75

print('TDA4vm Edge Impulse bag detector alert')
print('Roni Bandini Dec, 2022')

with open('bagdetectorlog.txt') as f:
	for line in f:
		myPosition=line.find(":0.")
		if myPosition>0:
			print("")
			print(line)
			myConfidence=line[ myPosition+3 : myPosition+3+2]
			print(myConfidence+"%")
			if (int(myConfidence)>myLimit):
				print("TDA4vm detected a bag!")
				telegramAlert("TDA4vm detected a bag "+myConfidence+"%")

		if 'str' in line:
			break

