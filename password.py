time = 3 #剩餘次數
password = 'a123456'
while time > 0:
	time = time - 1
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功！')
		break
	else:
		print('登入錯誤！')
		if time > 0:
			print('還有', time, '次機會')
		else:
			print('沒有機會了！')
