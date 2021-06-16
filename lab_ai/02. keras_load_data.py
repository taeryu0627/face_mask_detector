import tensorflow as tf
import matplotlib.pyplot as plt

train_dataset=tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='training',
    seed=999,
    image_size=(224,224),
    batch_size=16
    )

valid_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='training',
    seed=999,
    image_size=(224,224),
    batch_size=16
)

resize_and_crop = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomCrop(height=224, weights=224),
    tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
])

rc_train_dataset = train_dataset.map(lambda x, y: (resize_and_crop(x),y))
rc_valid_dataset = train_dataset.map(lambda x, y: (resize_and_crop(x),y))


plt.figure(0)
plt.title('train_dataset')
for images, labels in train_dataset.take(1):
    for i in range(9):
        plt.subplot(3, 3, i+1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(train_dataset.class_names[labels[i]])
        plt.axis('off')

plt.figure(1)
plt.title('valid_dataset')
for images, labels in valid_dataset.take(1):
    for i in range(16):
        plt.subplot(4, 4, i+1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(train_dataset.class_names[labels[i]])
        plt.axis('off')

plt.show()