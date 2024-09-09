import cv2
import face_recognition
import pickle
import os 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://attendanceprojectfr-default-rtdb.firebaseio.com/",
        "storageBucket": "attendanceprojectfr.appspot.com"
    }
)

#Importing students images
folderPathImages = 'Images'
listPathImages = os.listdir(folderPathImages)
imgListImages = []

studentIDs = []

for path in listPathImages:
  imgListImages.append(cv2.imread(os.path.join(folderPathImages, path)))

  studentIDs.append(os.path.splitext(path)[0])
  fileName = f'{folderPathImages }/{path}'

  bucket = storage.bucket()

  blob = bucket.blob(fileName)

  blob.upload_from_filename(fileName)



def generatorEncodings(images):

  encodingsList = []

  for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodingsList.append(encode)

  return encodingsList

encodingsListKnown = generatorEncodings(imgListImages)
encodingsListWithIDs = [encodingsListKnown, studentIDs]

encodingFile = open("EncodingsFile.p", "wb")
pickle.dump(encodingsListWithIDs, encodingFile)
encodingFile.close


