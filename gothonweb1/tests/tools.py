#encoding: utf-8
from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None,
headers=None, status="200"): #各变量设置默认值
	
	assert status in resp.status, "Expected response %r not in %r" %(status, resp.status)
	
	if status == "200":
		assert resp.data, "Rseponse data is empty." 
		
	if contains:
		assert contains in resp.data, "Rseponse dose not contain %r" % contains
	
	if matches:
		reg = re.compile(matches)
		assert reg.matches(resp.data), "Response does not match %r" % matches
		
	if headers:
		assert_equal(resp.headers, headers)
		