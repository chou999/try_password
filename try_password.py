i = 3
while i > 0:
    password = input('請輸入密碼：')
    i = i - 1
    if password == 'a123456':
    	print('登入成功！')
    	break # 逃出回圈
    else:
    	print('密碼錯誤！')
    	if i > 0:
    		print('你還有', i,'次機會！')
    	else:
    		print('你沒機會嘗試了！')

