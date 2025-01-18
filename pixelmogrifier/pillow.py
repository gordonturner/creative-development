#!/usr/local/bin/python3

from PIL import Image, ImageDraw
import numpy as np
from sklearn.cluster import KMeans

# Create an image with RGB mode
# image = Image.new('RGB', (100, 100), color = 'red')

image = Image.open(r"./output-images/eggplant-32.png") 
vec = np.array(image)

vec = vec.reshape(-1, 3)

# How many colours to include in our palette
numColors = 16

model = KMeans(n_clusters=numColors).fit(vec)
palette = model.cluster_centers_

n = len(palette)

im = Image.new('RGBA', (100*n, 100))
draw = ImageDraw.Draw(im)

for idx, color in enumerate(palette):
	color = tuple([int(x) for x in color])
	print(color)
	draw.rectangle([(100*idx, 0), (100*(idx+1), 100*(idx+1))],
				   fill=tuple(color))
im.show()

# Save the image
# image.save('output-palette.jpg')

# image.show()