import random


output_w = '<table align="center" bgcolor="white" border="0" cellpadding="4">\n\t<tr align="center" bgcolor="white" valign="middle">\n'
type1 = '\t\t<td bgcolor="white" align="center" colspan="1" rowspan="1">'
type2 = '\t\t<td align="center" bgcolor="white" colspan="1" rowspan="1">'
binary = ''

# Tool Based on HTML Steganography and Platinum APT
# By Astr0 


def encode():
	output = open('output.html', 'w+')
	text = str(input('[-] String to encode >>> '))
	global output_w
	#encoded = ' '.join(format(ord(x), 'b') for x in text)
	encoded = ""
	for x in text:
		if x == ' ':
			encoded += '0100000'
			
		else:
			encoded += f''.join(format(ord(x), 'b'))



	for number in encoded:
		if int(number) == 1:
			output_w += f'{type1}{random.randint(1,1000)}</td>\n'
		elif int(number) == 0:
			output_w += f'{type2}{random.randint(1,1000)}</td>\n'

	output_w += "\t</tr>\n</table>"
	print(encoded)


	print('[-] Creating HTML File (output.html) [-]')

	output.write(output_w)

	print('[-] Finished [-]')


def decode(s):

    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def decode_html():
	html = str(input('[-] Path al archivo HTML >>> '))
	html = open(html, 'r').read()
	splitted = html.split('<td ')
	global binary

	for td in splitted:
		if td[0] == 'b':
			binary += '1'
		elif td[0] == 'a':
			binary += '0'

	textnum = ""
	numcnt = 0

	for number in binary.split()[0]:
		textnum += number
		numcnt += 1	
		if numcnt == 7:
			numcnt = 0
			textnum += " "
		else:
			pass
		
	print(textnum)
	print(f'[-] DECODED: {decode(textnum)}')



def menu():

	print('Html Encoder by Asteriscos\n\n')
	print('[1] ENCODE STRINGS')
	print('[2] DECODE STRINGS\n')

	num = int(input('>>> '))
	if num == 1:
		encode()
	elif num == 2:
		decode_html()



if __name__ == "__main__":
    menu()