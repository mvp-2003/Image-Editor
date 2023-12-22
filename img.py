from PIL import Image, ImageEnhance, ImageFilter
import os

path_to_image=str(input("Enter image path: "))

for i in range(len(path_to_image)-1, -1, -1):
    if path_to_image[i]=='/':
        k = i

dest_path = path_to_image[:k+1]
image_name = path_to_image[k:]

if os.path.exists(path_to_image):
    image = Image.open(path_to_image)
    edited_image = image.filter(ImageFilter.DETAIL)
    edited_image = edited_image.filter(ImageFilter.SHARPEN).convert('L')
    edited_image = edited_image.filter(ImageFilter.SMOOTH)

    edit.save('dest_path/{clean_name}new{image_name}')