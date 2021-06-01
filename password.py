time = 3
while time > 0:
	time = time - 1
	password = input('請輸入密碼：')
	if password != 'a123456':
		print('密碼錯誤！還有', time, '次機會')
	elif password == 'a123456':
		print('登入成功')
		break
