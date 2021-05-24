#마스크 이미지를 원본 이미지에 합성하는 코드
import face_recognition
from PIL import Image, ImageDraw

#이미지 열어주기
image_path = '../data/without_mask/0.jpg'
mask_image_path = '../data/mask.png'

face_image_np = face_recognition.load_image_file(image_path) # 이미지를 일단 불러오기만,,
face_locations = face_recognition.face_locations(face_image_np, model='hog')
face_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_image)

for face_location in face_locations: # 각 얼굴 위치([(46, 114, 108, 52)])들이 face location 안에 들어감
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
mask_image = Image.open(mask_image_path)

a=int(((right+left)/2)-(right-left)//2)
b=int(bottom*(3/4))

num1=right-left
num2=(bottom-top)
mask_image = mask_image.resize((num1, num2))

draw.rectangle(((left, top), (right, bottom)), outline=(255,9,220), width=10)
face_image.paste(mask_image,(a,b), mask_image)
face_image.show()