from PIL import Image
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--input', dest='input_file', type=str, required=True)
parser.add_argument('--size', dest='pix_size', type=int, required=True)
parser.add_argument('--output', dest='output_file', type=str, required=True)

args = parser.parse_args()
background_color = (255,)*3

pix_size = args.pix_size

image = Image.open(args.input_file)
image = image.resize((image.size[0]//pix_size, image.size[1]//pix_size),
                     Image.NEAREST)
image = image.resize((image.size[0]*pix_size, image.size[1]*pix_size),
                     Image.NEAREST)
pixel = image.load()

for i in range(0, image.size[0], pix_size):
    for j in range(0, image.size[1], pix_size):
        for r in range(pix_size):
            pixel[i+r, j] = background_color
            pixel[i, j+r] = background_color

image.save(args.output_file, 'png')
