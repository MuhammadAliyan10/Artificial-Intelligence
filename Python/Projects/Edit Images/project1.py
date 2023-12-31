from PIL import Image,ImageEnhance,ImageFilter
import os

#---------------------------------------------->

# f = Image.open('img.jpg')
# f.save('img.png')
# f.show()

#-------------------------------------------->

# max_size = (250,250)
# f.thumbnail(max_size)
# f.save('img.jpg')

#------------------------------------------->

#We can make copy of these pic..
# for items in os.listdir():
#     if items.endswith('.jpg'):
#         img = Image.open(items)
#         filename,extension = os.path.splitext(items)
#         img.save(f"{filename}.png")


#-------------------------------------------->

#You can make the image shraper and to do this you need to import the module ImageEnhance
#At 0 Point ----> The pic will blur..
#At 1 Point ----> The pic will be orignel..
#At 2 Point ----> The pic will became sharp..
#At 3 Point ----> The pic will became more sharp..
# f = Image.open('img1.jpg')
# sharp = ImageEnhance.Sharpness(f)
# sharp.enhance(10).save('img1editied.jpg')


#-------------------------------------------->

#You can make the image colorfull and to do this you need to import the module ImageEnhance
#At 0 Point ----> The pic will black and white..
#At 1 Point ----> The pic will be orignel..
#At 2 Point ----> The pic will became color full..
#At 3 Point ----> The pic will became more color full..
# f = Image.open('img1.jpg')
# sharp = ImageEnhance.Color(f)
# sharp.enhance(4).save('img1editied.jpg')


#-------------------------------------------->

#You can change the brightness of the image and to do this you need to import the module ImageEnhance
#At 0 Point ----> The pic will black..
#At 1 Point ----> The pic will be orignel..
#At 2 Point ----> The pic will became color full..
#At 3 Point ----> The pic will became more color full..
# f = Image.open('img1.jpg')
# sharp = ImageEnhance.Brightness(f)
# sharp.enhance(4).save('img1editied.jpg')

#-------------------------------------------->

#You can change the contrast of the image and to do this you need to import the module ImageEnhance
#At 0 Point ----> The pic will low_contrased..
#At 1 Point ----> The pic will be orignel..
#At 2 Point ----> The pic will became color full..
#At 3 Point ----> The pic will became more color full..
# f = Image.open('img1.jpg')
# sharp = ImageEnhance.Contrast(f)
# sharp.enhance(-10).save('img1editied.jpg')



#-------------------------------------------------->

#To blur the image you can import the module ImageFilter
#By default radius is 2 so we can change the radius
f = Image.open('img1.jpg')
f.filter(ImageFilter.GaussianBlur(radius= 4)).save('img1blur.jpg')