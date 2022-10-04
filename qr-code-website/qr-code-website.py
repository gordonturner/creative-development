#!/usr/local/bin/python3

import argparse
from typing import List
from qrcodegen import QrCode, QrSegment

def to_svg_str(qr: QrCode, border: int) -> str:
	"""Returns a string of SVG code for an image depicting the given QR Code, with the given number
	of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
	if border < 0:
		raise ValueError("Border must be non-negative")
	parts: List[str] = []
	for y in range(qr.get_size()):
		for x in range(qr.get_size()):
			if qr.get_module(x, y):
				parts.append("M{},{}h1v1h-1z".format(x + border, y + border))
	return """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {0} {0}" stroke="none">
	<rect width="100%" height="100%" fill="#FFFFFF"/>
	<path d="{1}" fill="#000000"/>
</svg>
""".format(qr.get_size() + border * 2, " ".join(parts))

parser = argparse.ArgumentParser(description='Create a qr code.')

parser.add_argument('-i', 
					type=str, 
					required=False,
                    default='data.txt',
                    help='input data file to parse, example data.txt')

parser.add_argument('-o', type=str, 
					required=False,
                    default='qr-code-website.svg',
                    help='output svg filename, defaults to "qr-code-website.svg"')

args = parser.parse_args()
print('Input filename:  ', args.i)
print('Output filename: ', args.o)

toEncode = 'EMPTY'

# Read in the input file to get the value to encode, the second line.
with open(args.i) as file:
    lines = file.readlines()
    toEncode = lines[0].rstrip()
    	
print('Value to encode: ', toEncode)

qr = QrCode.encode_text(toEncode, QrCode.Ecc.LOW)

file = open(args.o, "w")
file.write(to_svg_str(qr, 0))
file.close()

