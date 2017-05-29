# This Converts ASCII text into Byte Form
import binascii

def byte_me(text):

	#text = raw_input("Enter your Text of ASCII Characters: ")
	bin_text = [0]*len(text) #PreAllocation

	def ascii_to_bin(char):
		return bin( int( binascii.hexlify(char),16))

	def text_to_bin():
		index = 0
		while index < len(bin_text):
			bin_text[index] = ascii_to_bin(text[index])

			# Make Sure to Include Full Byte
			if len( bin_text[index] ) < 9:
				# Consider Modifying indexing for more flexibility with Binary Transormation
				bin_text[index] = bin_text[index][0:2] + '0' + bin_text[index][2: len(bin_text[index])]
			index += 1

	text_to_bin()

	text_bytes = []
	for num in range(len(bin_text)):
		for char in bin_text[num]:
			if char != 'b':
				text_bytes += char

	return text_bytes