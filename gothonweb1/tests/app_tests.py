from nose.tools import *
from bin.app import app
from gothonweb import map
from tests.tools import assert_response

def test_index():
	#check that we get a 303 on the / URL

	resp = app.request("/")
	assert_response(resp, status="303")
	

def test_GameEngine():	
	# test our first GET request to /hello
	resp = app.request("/game")
#	print resp.data
	assert_response(resp, status="200",contains="You Died")
	
	# make sure default values work for the form
	resp = app.request("/game", method="POST")
	assert_response(resp, status="303", contains=None)
	
	# test that we get expected values
#	data = {'name': 'Zed', 'greet': 'Hola'}
	data = {'action': 'go'}
	resp = app.request("/game", method="POST", data=data)
#	print resp.data
	assert_response(resp,status="303", contains='go')
	
