# made by 志在南七


# 二进制除法（异或运算），只返回了余数，商也可返回
def binary_division(s1, s2):
	while (len(s1) >= len(s2)):
		sub_s1 = s1[:len(s2)]
		result = '' # 商
		if sub_s1[0] == '0':
			s1 = s1[1:]
			result = result + '0'
		else:
			a = ''
			for i in range(len(s2)):
				if sub_s1[i] == s2[i]:
					a = a + '0'
				else:
					a = a + '1'
			result = result + '1'
			s1 = a[1:] + s1[len(s2):]
	remainder = s1
	return remainder

def CRC_generator(source_s, generator_s):
	# source_s: 源串
	# generator_s:生成多项式。最高位必须为1
	if generator_s[0] != '1':
		return None
	g_len = len(generator_s)
	# 末尾补零
	source_s_zero = source_s + '0' * (g_len - 1)
	remainder = binary_division(source_s_zero, generator_s)
	# 余数至末尾
	crc_code = source_s + remainder
	return crc_code

def CRC_check(crc_code, generator_s):
	remainder = binary_division(crc_code, generator_s)
	if remainder == '0' * (len(generator_s) - 1):
		return '你码对了'
	else:
		return '你码炸了'

rate = 0.5

a = CRC_generator('10101011', '10011')
print(CRC_check(a, '10011'))
print(CRC_check(a+'1', '10011'))




