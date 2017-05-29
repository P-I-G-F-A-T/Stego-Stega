# Masks Text Into PNG
from PIL import Image
from PIL import ImageColor

import TextToByte2
import operator

SOURCE = raw_input("Type in the file (make sure in same path): ")
#text = open(SOURCE,'r')
#text = text.read()
text = raw_input("Type in your message: ")

bit_string = TextToByte2.byte_me(text)

base = Image.open(SOURCE)
width, height = base.size

text_index = 0
for x in range (width):
		for y in range (height):
			# Grabs RGBA Value at Coordinate (x,y)
			# Then Converts Value into List
			pixel = base.getpixel( (x,y) )
			pixel_list = list(pixel)

			try:
				# Work Through The 4 Components - RGBA
				for combination_index in range(4):
					# Pixel List Value (Index 0,1,2,3) Added to Bit Value (Increment from Starting Point to Starting Point+3)
					pixel_list[combination_index] += int( bit_string[text_index] )
					text_index+=1

					# SOURCE Pixel w/ New Pixel List Value Replace (Each Time)
					base.putpixel( (x,y), tuple(pixel_list) )

			# If it Cannot Work Through, then stop the looping
			except IndexError:
				NEW_SOURCE = "Stego" + SOURCE[4:len(SOURCE)]
				base.save(NEW_SOURCE)
				quit()
