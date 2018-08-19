from PIL import Image, ImageChops, ImageDraw

def autotrim(image1):
    width, height = image1.size
    isPhoto = False
    for h in range(height):
        if(isPhoto == False):
            for w in range(width):        
                r,g,b = image1.getpixel((w,h))
                """Detects the Top Left Corner of the Image"""
                if((r<230 or g<230 or b<230)):
                    topLeftHeight = h+1
                    topLeftWidth = w+1
                    isPhoto = True
                    break
        else:
            break;
    
    """Detects the Top Right Corner of the Image"""
    for w in range(topLeftWidth,width):
        r,g,b = image1.getpixel((w,topLeftHeight))

        if(r>230 and g>230 and b>230):
            bottomRightWidth = w
            break

    """Detects the Bottom Left Corner of the Image"""
    for h in range(topLeftHeight,height):
        r,g,b = image1.getpixel((topLeftWidth,h))

        if(r>230 and g>230 and b>230):
            bottomRightHeight = h
            break

    print((topLeftWidth-1, topLeftHeight-1, bottomRightWidth, bottomRightHeight))
    croppedImage = image1.crop((topLeftWidth, topLeftHeight, bottomRightWidth, bottomRightHeight))
    draw = ImageDraw.Draw(image1)
    croppedImage.show()
    draw.rectangle((topLeftWidth-12, topLeftHeight-12, bottomRightWidth+3, bottomRightHeight+3),fill = "white",outline = "white")
    return image1


image = Image.open('multiple.jpg')
for i in range(3):
    image = autotrim(image)
    
