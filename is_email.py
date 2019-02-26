import re
def is_valid_email(add):
	if re.match(r'[\w\.]+\@\w+\.(com|cn)', add):
		return True
	else:
		return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


def name_of_email(add):
	email = re.match(r'^\<?([a-zA-z]+\s?[a-zA-Z]+)\>?[\w\s]*\@\w+\.(com|cn|org)', add)
	if email:
		return email.group(1)
	else:
		return None

print(name_of_email('<Tom Paris> tom@voyager.org'))

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')