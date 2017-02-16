from PIL import Image
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--input', '-i', dest='input_file', type=str,
                    required=True)
parser.add_argument('--output', '-o', dest='output_file', type=str,
                    required=True)
parser.add_argument('--mask', '-m', dest='mask_file', type=str)
parser.add_argument('--background', '-b', dest='background_color', type=str,
                    default='#000000')

args = parser.parse_args()

background_color = args.background_color.strip('#')
background_color = tuple([int(background_color[i:i+2], 16) for i in (0, 2, 4)])

if args.mask_file:
    mask = Image.open(args.mask_file)
else:
    mask = Image.new('RGBA', (24, 24), color=(255, 255, 255, 0))

image = Image.open(args.input_file)
image = image.resize((image.size[0]//mask.size[0],
                      image.size[1]//mask.size[1]),
                     Image.NEAREST)

image = image.resize((image.size[0]*mask.size[0], image.size[1]*mask.size[1]),
                     Image.NEAREST)

solid_background = Image.new('RGBA', mask.size,
                             color=background_color + (255,))

for i in range(0, image.size[0], mask.size[0]):
    for j in range(0, image.size[1], mask.size[1]):
        image.paste(solid_background, (i, j), mask)


image.save(args.output_file, 'png')
