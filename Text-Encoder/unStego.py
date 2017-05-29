SOURCE = raw_input("What is the source txt file: ")
text = open(SOURCE,'r')
line = 'initialization'
message = ''

while True:
	try:
		line = text.readline()
		message = message + chr( int(line,2))
	except ValueError:
		break

message_mod = ''
character = ''
counter = 0

while character != '\x00':
	character = message[counter]
	message_mod = message_mod + character
	counter +=1

print message_mod