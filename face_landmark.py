# 얼굴 랜드마크 추출

import face_recognition
from PIL import Image, ImageDraw

face_image_path = 'data/without_mask/127.jpg'
mask_image_path = 'data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)

maxX = 0
maxY = 0
minX = 10000
minY = 10000

for face_landmark in face_landmarks:
   for feature_name, points in face_landmark.items():
       print(feature_name,points)
       if feature_name == "chin":
           for x, y in points:
               if minX > x:
                   minX = x
               if minY > y:
                   minY = y
               if maxX < x:
                   maxX = x
               if maxY < y:
                   maxY = y

print(maxX,minX,maxY,minY)

for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

mask_image_np = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(mask_image_np)

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((int(maxX)-int(minX),int(maxY)-int(minY)))

face_landmark_image.paste(mask_image,(int(minX), int(minY)),mask_image)


face_landmark_image.show()
