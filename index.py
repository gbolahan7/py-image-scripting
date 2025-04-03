from PIL import Image, ImageFilter

img = Image.open('images/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
filtered_img2 = img.resize((300, 300))
filtered_img.save("grey.png", "png")

box = (100, 100, 400, 400)
area = filtered_img.crop(box)
area.show()
# print(img.format)
# filtered_img.show()
# filtered_img2.show()

