import os
from wand.image import Image
import cv2

class pdf_to_png(object):
	def __init__(self, filename, num_pages):
		self.Filename = filename
		self.Num_pages = num_pages

	def clean_image(self, filename):
		image = cv2.imread(filename)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gray = cv2.threshold(gray, 0, 255, 
							cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		gray = cv2.medianBlur(gray, 3)

		cv2.imwrite(filename, gray)
		print('Cleaning applied.')

	def convert(self, filename, num_pages):
		for i in range(num_pages):
			with Image(filename=(filename + '[' + str(i) + ']'), resolution=500) as img:
				with Image(width=img.width, height=img.height) as bg:
					bg.composite(img,0,0)
					print('PDF to PNG conversion complete for page ' + str(i) +'.')
					bg.save(filename='image' + str(i) + '.png')
					self.clean_image('image' + str(i) + '.png')