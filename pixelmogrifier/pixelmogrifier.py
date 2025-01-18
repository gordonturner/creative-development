#!/usr/local/bin/python3

import argparse
from typing import List
import cv2

parser = argparse.ArgumentParser(description='Take an image and pixel-ize it.')

parser.add_argument('-i', 
                    type=str, 
                    required=False,
                    default='input.jpg',
                    help='input image file')

parser.add_argument('-o', type=str, 
                    required=False,
                    default='output.jpg',
                    help='output jpg filename, defaults to "output.svg"')

# TODO: Add image height and width dimension arguements

args = parser.parse_args()
print('Input filename:  ', args.i)
print('Output filename: ', args.o)

# Input image
input = cv2.imread(args.i)

# Get input size
height, width = input.shape[:2]

# Desired "pixelated" size
# w, h = (64, 64)
w, h = (32, 32)
# w, h = (24, 24)
# w, h = (16, 16)

# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

# Write to file
cv2.imwrite(args.o, output)

cv2.imshow('Input', input)
cv2.imshow('Output', output)

cv2.waitKey(0)