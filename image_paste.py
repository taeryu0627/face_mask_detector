import face_recognition
from PIL import Image, ImageDraw

face_image_path = 'data/without_mask/0.jpg'
mask_image_path = 'data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_image)

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((63,50))

face_image.paste(mask_image,(53,60),mask_image)
face_image.show()