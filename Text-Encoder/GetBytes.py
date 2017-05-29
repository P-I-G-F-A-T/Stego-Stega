# This Program Converts uses the pixel values
# to create a file of bytes (evens=>0 and odds=>1)
from PIL import Image
import operator

# SOURCE is the desired image. Mind your directories.
SOURCE = raw_input("Enter in the file name (must be in the same directory): ")
base = Image.open(SOURCE)
width, height = base.size

# Prepare to Store Info in Texts
file1 = "Masked"+ SOURCE
file1 = file1[:-4]
file1 = file1 + '.txt'

text = open(file1,'w')
counter = 0

for x in range (width):
	for y in range (height):
		pixel = base.getpixel( (x,y) )

		# Preallocate Pixel Modifier
		pixel_mod = [0]*len(pixel)

		# If Pixel Value is Odd, make Even
		for index in range( len(pixel)):
			if pixel[index]%2 == 1:
				pixel_mod[index] = 1

		# Setup for Text File
		listed = ""

		# The Counter is used to properly space the Bytes with '\n'
		if counter == 0:
			# The program writes each pixel's parity into 'listed'
			# So listed becomes a string of 4 bits
			# Then listed is written into the text file
			for val in pixel_mod:
				listed = listed + str(val)
			text.write( listed )

			counter = 1

		else:
			for val in pixel_mod:
				listed = listed + str(val)

			# '\n' will ensure there is exactly one byte per line in the txt file
			text.write( listed + '\n' )
			
			# Now the counter resets to 0 and the loop begins again
			counter = 0
text.close()