#!/usr/local/bin/python3

from colorthief import ColorThief
from PIL import Image, ImageDraw

color_thief = ColorThief('./output-images/eggplant-32.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=16)
# print(palette)

n = len(palette)

im = Image.new('RGBA', (100*n, 100))
draw = ImageDraw.Draw(im)

for idx, color in enumerate(palette):
	color = tuple([int(x) for x in color])
	print(color)
	draw.rectangle([(100*idx, 0), (100*(idx+1), 100*(idx+1))],
				   fill=tuple(color))

im.show()