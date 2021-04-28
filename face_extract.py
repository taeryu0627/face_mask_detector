import face_recognition
from PIL import Image, ImageDraw

image_path = 'data/without_mask/0.jpg'
mask_image_path = 'data/mask.png'

face_image_np = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(face_image_np)

face_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_image)

for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

mask_image_np = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(mask_image_np)

mask_locationY = int((bottom+top)/3)
mask_locationX = int((right+left)/3)

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((right-left,bottom-top))
print(str(mask_locationY)+', '+str(mask_locationX))

face_image.paste(mask_image,(mask_locationX,mask_locationY),mask_image)




face_image.show()