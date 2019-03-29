
import argparse
import os
from os.path import join
from PIL import Image

def resize_image(input_file, output_file, size=(320, 180)):

    try:
        if (input_file[-4:] == ".jpg"):
            img = Image.open(input_file)
            img = img.resize((size[0], size[1]), Image.LANCZOS)

            img.save(output_file)
    except IOError:
        print("unable to resize image {}".format(input_file))


if __name__ == "__main__":

    dir = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', help='Full Input Path')
    parser.add_argument('-o', '--output_dir', help='Full Output Path')
    args = parser.parse_args()

    if args.input_dir:
        input_dir = args.input_dir
    else:
        input_dir = dir + '/images/downloads'

    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = dir + '/images/resized'

    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)

    try:
        for root, dirs, files in os.walk(input_dir):
            folder = root[len(input_dir):]
            for file in files:
                input_file = (input_dir + folder + "\\" + file).replace("/", "\\")
                output_file = (output_dir + folder + "\\" + file).replace("/", "\\")
                output_folder = (output_dir + folder).replace("/", "\\")
                if not os.path.exists(output_folder):
                    os.mkdir(output_folder)
                resize_image(input_file, output_file)
    except OSError:
        print('file not found')

