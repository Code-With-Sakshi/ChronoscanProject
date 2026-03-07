import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# -----------------------
# CONFIG
# -----------------------
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 10

# -----------------------
# DATA LOADING
# -----------------------
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train = datagen.flow_from_directory(
    "../archive",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="training"
)

val = datagen.flow_from_directory(
    "../archive",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="validation"
)

# -----------------------
# MODEL
# -----------------------
model = models.Sequential([
    layers.Conv2D(32, 3, activation="relu", input_shape=(224,224,3)),
    layers.MaxPooling2D(),

    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(128, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# -----------------------
# TRAIN
# -----------------------
history = model.fit(
    train,
    validation_data=val,
    epochs=EPOCHS
)

# -----------------------
# SAVE MODEL
# -----------------------
model.save("brain_tumor_model.h5")

# -----------------------
# ACCURACY RESULTS
# -----------------------
train_acc = history.history["accuracy"][-1]
val_acc = history.history["val_accuracy"][-1]

print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Validation Accuracy: {val_acc * 100:.2f}%")

# -----------------------
# PLOT ACCURACY
# -----------------------
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Tumor Detection Accuracy")
plt.legend()
plt.show()


