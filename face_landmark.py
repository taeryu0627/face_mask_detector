# 얼굴 랜드마크 추출

import face_recognition
from PIL import Image, ImageDraw

face_image_path = 'data/without_mask/104.jpg'
mask_image_path = 'data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)

for face_landmark in face_landmarks:
   for feature_name, points in face_landmark.items():
       print(feature_name,points)

# x값
maskLeft = face_landmarks[0]['chin'][0][0]
maskRight = face_landmarks[0]['chin'][16][0]
mask_xsize = abs(maskRight-maskLeft)

# y값
maskUp = face_landmarks[0]['nose_bridge'][0][1]
maskDown = face_landmarks[0]['chin'][8][1]
mask_ysize = abs(maskUp-maskDown)

mask_image = Image.open(mask_image_path)

mask_image = mask_image.resize((mask_xsize, mask_ysize))
face_landmark_image.paste(mask_image, (maskLeft,maskUp), mask_image)

mask_image_np = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(mask_image_np)

face_landmark_image.show()
