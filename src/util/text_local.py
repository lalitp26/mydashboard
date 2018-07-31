#!/usr/bin/env python
 
import urllib.request
import urllib.parse

def sendSMS(numbers, sender, message):
	apikey = 'aPdWUtBpRbo-F12WabGmzCvcnBewd82sovw3hVtfbv'

	data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender})
	data = data.encode('utf-8')
	request = urllib.request.Request("https://api.textlocal.in/send/?")
	f = urllib.request.urlopen(request, data)
	fr = f.read()
	return(fr)
 

