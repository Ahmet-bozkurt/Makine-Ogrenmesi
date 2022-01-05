import cv2
import os
import numpy as np
from tensorflow.keras.models import model_from_json

dizin = os.getcwd()

yuz_tanima = cv2.CascadeClassifier("yuz_tanima/haarcascade_frontalface_default.xml")
# model kaynağı olan json dosyası tanımlama için
model_kaynak = open('siniflandirma_modeli/model_save.json')
model_json = model_kaynak.read()
model_kaynak.close()
model = model_from_json(model_json)
# model eğitimi sonucunda elde ettiğimiz değerler dosyası olan h5 uzantılı dosyanın eklenmesi
model.load_weights('siniflandirma_modeli/model_save_191-0.989474.h5')

print("Model ve kaynak dosyası başarı ile yüklendi.")

video = cv2.VideoCapture(0)

while True:
    try:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = yuz_tanima.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = frame[y - 5:y + h + 5, x - 5:x + w + 5]
            resized_face = cv2.resize(face, (160, 160))
            resized_face = resized_face.astype("float") / 255.0
            # algılanan yüz görüntüsünü bir numpy dizisi haline getirmek için
            resized_face = np.expand_dims(resized_face, axis=0)
            # elde ettiğimiz numpy dizisini modelimize veriyoruz ve gerekli
            # özellik çıkarımı yaptıkta sonra bize float bir sayı dönderecek
            # bu sayı 0.05 den büyükse bu görüntünün sahte olduğunu anlayacağız
            preds = model.predict(resized_face)[0]
            print(preds)
            if preds > 0.05:
                label = 'Sahte Goruntu'
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            else:
                label = 'Gercek Goruntu'
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except Exception as e:
        pass
video.release()
cv2.destroyAllWindows()