### CS50 T-Shirt - I want one tshirt too!
import sys
from PIL import Image
from PIL import ImageOps


def main():
    try:
        filename1, ext1 = sys.argv[1].split('.')
        filename2, ext2 = sys.argv[2].split('.')
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        elif len(sys.argv) >3:
            sys.exit('Too many command-line arguments')
        elif sys.argv[2].lower().endswith(('.jpg', '.jpeg', '.png')) == False:
            sys.exit('Invalid output')
        elif ext1.lower() != ext2.lower():
            sys.exit('Input and output have different extensions')

        else:
            shirt_printer(sys.argv[1], sys.argv[2])
    except(FileNotFoundError):
        sys.exit('Input does not exist')


def shirt_printer(a, b):
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = Image.open(a)
    photo_resize = ImageOps.fit(photo, size)
    photo_resize.paste(shirt,shirt)
    photo_resize.save(b)


if __name__ == "__main__":
    main()



### 4 tries
# def shirt_printer(a, b):

#     photo = Image.open(a)
#     photo_resize = ImageOps.fit(photo, size)
#     shirt = Image.open("shirt.png")
#     #size = shirt.size
#     #photo_size = photo.size
#     #print(photo_size)
#     #shirt_resize = ImageOps.fit(shirt, (600, 600),centering=(0.5,0.5))
#     shirt_resize = shirt.resize((600, 600),resample=None,reducing_gap=None)
#     photo_resize.paste(shirt_resize, (600, 600) shirt_resize)
#     photo_resize.save(b)
