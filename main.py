from PIL import Image 
import matplotlib.pyplot as plt
from PIL import ImageFilter
picture = "original.jpg"
with Image.open(picture) as original:
    print(original.mode)
    print(original.format)
    print(original.size)
    plt.imshow(original)
    plt.show()
  
pic_gray = original.convert('L')
pic_gray.save('gray.jpg')
pic = 'gray.jpg'
with Image.open(pic) as gray:
    print(gray.mode)
    print(gray.format)
    print(gray.size)
    plt.imshow(gray)
    plt.show()


pic_blur = original.filter(ImageFilter.BLUR)
pic_blur.save('blured.jpg')
img = 'blured.jpg'
with Image.open(img) as blur:
    print(blur.mode)
    print(blur.format)
    print(blur.size)
    plt.imshow(blur)
    plt.show()

pic_upside = original.transpose(Image.ROTATE_180)
pic_upside.save('up.jpg')
image = 'up.jpg'
with Image.open(image) as up:
    print(up.mode)
    print(up.format)
    print(up.size)
    plt.imshow(up)
    plt.show()


