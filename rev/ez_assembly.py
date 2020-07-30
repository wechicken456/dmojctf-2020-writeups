
enc = "|A4$wb!Of(O6H>5PQ?6Tb&CJEHELIK?6a~BP?"
flag_len = len(enc)


# ---------	First round - which is the last encryption block -----------------

j = flag_len-1
dec_1 = [None]*flag_len

for i in range(18):
	dec_1[i] = enc[j]
	dec_1[j] = enc[i]
	j -= 1
dec_1[18] = enc[18]	# because i will only go up to 17 and j will only go down to 19 => 18th is unaffected
#print("Flag after 1st decryption round: " + "".join(dec_1))


# --------- Second round -----------------

flag = ["" for i in range(flag_len)]
for i in range(len(dec_1)):
	if dec_1[i] == '|':
		flag[i] = ord('}')
	elif dec_1[i] == '~':
		flag[i] = ord('{')
	elif ord(dec_1[i]) >= ord('!') and ord(dec_1[i]) <= ord('!')+9:
		flag[i] = ord('_')
	else:
		if ord(dec_1[i]) - 0x1d >= ord('A') and ord(dec_1[i]) - 0x1d<= ord('Z'):
			flag[i] = ord(dec_1[i]) - 0x1d
		elif ord(dec_1[i]) + 0x24 >= ord('a') and ord(dec_1[i]) + 0x24 <= ord('z'):
			flag[i] = ord(dec_1[i]) + 0x24
		elif ord(dec_1[i]) >= ord('0') and ord(dec_1[i]) <= ord('9'):
			flag[i] = ord('i') - ord(dec_1[i])
		
print("".join([chr(i) for i in flag]))

