# This Program Rounds all the RGBA Values of an Image.
from PIL import Image
from PIL import ImageColor
import operator

# SOURCE is the desired image. Mind your directories.
SOURCE = raw_input("Enter in the file name (must be in the same directory): ")
base = Image.open(SOURCE)
width, height = base.size

# Check to see if Image is Appropriate Format
pixel = base.getpixel( (1,1))

if len(pixel) < 4:
	# Just Incase Length is 3 (Alpha is Default)
	base.alpha(255)
	pixel = base.getpixel( (x,y) )

for x in range (width):
	for y in range (height):
		pixel = base.getpixel( (x,y) )

		# Use to Modify Pixels in Stego
		pixel_mod = [0,0,0,0]

		# If Pixel Value is Odd, make Even
		for index in range( len(pixel)):
			if pixel[index]%2 == 1:
				pixel_mod[index] = -1

		# Write Pixel Mode back into Image
		pixel_mod = tuple(pixel_mod)
		new_pixel = tuple( map(operator.add,pixel,pixel_mod) )
		base.putpixel( (x,y),new_pixel )

NEW_SOURCE = "EVENIMAGE.png"
base.save(NEW_SOURCE)