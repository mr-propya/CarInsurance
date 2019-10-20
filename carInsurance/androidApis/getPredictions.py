from carInsurance import settings
import cv2,numpy as np
import tensorflow as tf

def predict(path):
    modelPath = settings.BASE_DIR + "\Predictions\CarsModel.h5"
    path = str(path).replace("/","\\")
    modelPath = str(modelPath).replace("/","\\")
    imagePath = settings.BASE_DIR+path
    print(imagePath)
    print(modelPath)
    test_image = convert_image(imagePath)
    test_imageX = (np.expand_dims(test_image / 255, 0))
    test_imageX = np.array(test_imageX).reshape(-1, 100, 100, 1)
    # print(test_imageX.shape)
    # with keras.utils.CustomObjectScope({'GlorotUniform': keras.initializers.glorot_uniform()}):
    #     model = keras.models.load_model(modelPath)
    #     prediction = model.predict(test_imageX)
    #     print(prediction)
    model = tf.keras.models.load_model(modelPath)
    predictions = model.predict(test_imageX)
    pred = dict()
    CATEGORIES = ['front_major', 'front_minor', 'front_moderate', 'rear_major', 'rear_minor', 'rear_moderate',
                  'side_major', 'side_minor', 'side_moderate', 'whole']
    for i in range(len(CATEGORIES)):
        pred[CATEGORIES[i]]=predictions[0][i]
    maxResults = dict()
    maxResults["maxResult"] = CATEGORIES[int(np.argmax(predictions[0]))]
    maxResults["maxProb"] = predictions[0][int(np.argmax(predictions[0]))]
    pred["max"] = maxResults
    return pred


def convert_image(image):
    IMG_SIZE=100
    img_array=[]
    try:
        img_array=cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        img_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
    except:
        pass
    return img_array


