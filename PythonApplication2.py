from PIL import Image, ImageChops, ImageFilter

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    else:
        print("No image detected")


image1 = Image.open('multiple.jpg')
width, height = image1.size
print( width)
#image2 = trim(image1)

#image2.show()
#image1.save('newfox.jpg')


