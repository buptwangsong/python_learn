# -*- coding: utf-8 -*-
import base64

def safe_base64_decode(s):
	lost_number = 4 - len(s)%4
	for x in range(lost_number):
		s += b'='

	return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')