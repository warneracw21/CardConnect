import textract
import argparse
import os 
#from wand.image import Image
from pdf_to_png import pdf_to_png

parser = argparse.ArgumentParser()

parser.add_argument('-t', action='store', dest='type', required='true',
					help='This is the input file type (PDF, XLSX, PNG etc..)')

parser.add_argument('-f', action='store', dest='input_file', required='true',
					help='This is the input file name.')

#parser.add_argument('-o', action='store', dest='output_file', 
					#help='This is the output file name.')


parser.add_argument('-v', action='version', version='%(prog)s 1.0')





args = parser.parse_args()

type_of_file = str(args.type)
input_file_name = str(args.input_file)


def validate_input(file_name):

	try:
		with open(file_name) as input_file:
			return true

	except OSError as e:
		return false



def process_PDF(file_name):

	path = os.path.dirname(os.path.realpath(__file__))

	text = textract.process()

#converter = pdf_to_png(filename=input_file_name, num_pages=7)
#converter.convert(filename=input_file_name, num_pages=7)

#def determine_PDF(file_name):
	#return 0



text = textract.process('/Users/seanparsons/Desktop/CardConnect_Project/image3.png', 
						encoding='ascii', language='eng')
text = str(text)

text = text.replace('\\n', "\n")

print(text)