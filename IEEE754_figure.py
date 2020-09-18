

# IEEE754 基于字符串操作 
# made by 志在南七
'''
后面会加上真值到二进制的转化，进而真值到IEEE754浮点数的转化
'''


# 16进制转化为2进制
def hex_to_binary(s):
	if len(s) != 8:
		print('please input 8 hex data')
		return 1
	hex = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
	new_s = ''
	for i in range(8):
		a = ord(s[i])
		if a > 47 and  a < 64:
			a = a - 48
		elif a > 64 and a < 97:
			a = a - 65 + 10
		elif a >= 97:
			a = a - 97 + 10
		new_s = new_s + hex[a]
	return new_s

# 二进制转化为真值
def binary_to_true(s):
	a = len(s)
	num = 0
	for i in range(a):
		if s[i] not in ['0', '1']:
			print('please input a number that is binary!')
			return None
		num += int(s[i]) * 2**(a-i-1)	
	#print('IEEE754:', s, '   true:', str(num))
	return num

# IEEE754浮点数转化为真值
def IEEE754_to_true(s):
	# 数符
	minues = int(s[0])
	# 阶码
	multi = binary_to_true(s[1:9]) - 127
	# weishu
	tail_s = '1' + s[9:]
	tail = binary_to_true(tail_s) * 2**(-23)
	#print(minues, tail, multi)
	return (-1)**minues * tail * 2**(multi)

def true_to_IEEE754():
	pass

# 无符号二进制加法
def binary_add(s1, s2):
	if len(s1) != len(s2):
		print('it must be same length!')
	com = ''
	c = 0
	for i in range(len(s1)):
		a = int(s1[len(s1)-i-1])
		b = int(s2[len(s2)-i-1])
		if (a + b + c) % 2 == 1:
			ans = 1
		else:
			ans = 0
		if (a + b + c) > 1 :
			c = 1
		else:
			c = 0
		com = str(ans) + com
	#com = str(c) + com
	return com

# 原码补码互相转化
def ori_to_dev(s):
	if s[0] == '0':
		return s
	new_s = ''
	one = '1'
	new_s = new_s + s[0]
	for i in range(1, len(s)):
		if s[i] == '1':
			new_s = new_s + '0'
		else:
			new_s = new_s + '1'
		one = '0' + one
	new_s = binary_add(new_s, one)
	return new_s

# 有符号二进制加法 输入为原码，输出为补码。dou=0为单符号位 1为双符号位
def binary_figure(s1, s2, dou=0):
	if dou == 0:
		s1, s2 = ori_to_dev(s1), ori_to_dev(s2)
	else:
		s1, s2 = s1[0] + ori_to_dev(s1[1:]), s2[0] + ori_to_dev(s2[1:])
	return binary_add(s1, s2)

# IEEE754浮点数计算   输入为符合IEEE754的32位二进制数，输出真值
# 虽然有基于二进制计算的库函数，但是并为使用。严格使用IEEE的计算标准。对阶，尾数求和，规格化，舍入（恒0），溢出判断（基于双符号位）
def IEEE754_figure(s1, s2):
	# duijie
	mul1 = binary_to_true(s1[1:9]) - 127
	mul2 = binary_to_true(s2[1:9]) - 127
	
	tail1 = '1' + s1[9:]
	tail2 = '1' + s2[9:]
	
	if mul1 > mul2:
		while(mul1 !=  mul2):
			tail2 = '0' + tail2[:-1]
			mul2 += 1
	if mul2 > mul1:
		while(mul1 != mul2):
			tail1 = '0' + tail1[:-1]
			mul1 += 1
	mul_com = mul1
	#print(mul1, mul2)
	# weishuqiuhe
	# double sign
	tail1 = s1[0]*2 + tail1
	tail2 = s2[0]*2 + tail2
	
	tail_com = binary_figure(tail1 , tail2, dou =1)
	#print('t',tail_com)
	if tail_com[:2] == '01':
		tail_com = '0' + tail_com[:-1]
		mul_com += 1
	if tail_com[:2] == '10':
		tail_com = '1' + tail_com[:-1]
		mul_com += 1
	#print(tail1, tail2, tail_com)
	minues = int(tail_com[0])
	tail_com = ori_to_dev(tail_com[1:])
	tail_true = binary_to_true(tail_com[1:]) * 2**(-23)
	
	#print(tail_com, tail_true, mul_com)
	return (-1)**minues * tail_true * 2**(mul_com)
	
			
#print(binary_figure('11101', '10111'))
#print(hex_to_binary('c6400000'))
print(IEEE754_to_true(hex_to_binary('c1040000')))
print("result:", IEEE754_figure(hex_to_binary('c1040000'), hex_to_binary('c1840000')))



