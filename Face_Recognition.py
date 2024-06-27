import cv2
import os
from datetime import datetime
import time
import face_recognition
import numpy as np
import csv

#Defining path of working directory
path = 'C:/Users/madhu/Desktop/FACE RECOGNITION/Faces'
csv_path = "C:/Users/madhu/Desktop/FACE RECOGNITION/CSV"

Known_Encodings =[]
Names =[]

List = os.listdir(path)

#Creating Name List and Encoding Image List
for img in List:
    Names.append(os.path.splitext(img)[0])
    Img_Load = face_recognition.load_image_file(f'{path}/{img}')
    Img_Encode = face_recognition.face_encodings(Img_Load)[0]
    Known_Encodings.append(Img_Encode)

#Creating CSV file
now = datetime.now()
cur_date = now.strftime("%Y-%m-%d")
f=open(os.path.join(csv_path, cur_date+'.csv'), 'w+', newline = '')


#Function to Mark Attendence
def markAttendance(name):
    cur_date = now.strftime("%Y-%m-%d")
    with open(os.path.join(csv_path, cur_date+'.csv'),'r+') as f:
        lnwriter = csv.writer(f)
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            cur_time = now.strftime("%H : %M : %S")
            lnwriter.writerow([name, cur_time])

#Lists for storing data captured using webcam
face_locations = []
face_encodings = []
face_names = []



cap = cv2.VideoCapture(0)

while True:
    #start_time = time.time()
    ret, frame = cap.read()
    small_frame = cv2.resize(frame,(0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    if True:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(Known_Encodings, face_encoding)
            face_dist = face_recognition.face_distance(Known_Encodings, face_encoding)
            match_index = np.argmin(face_dist)
            name = "Unknown"
            if matches[match_index]:
                name = Names[match_index]
            else:
                name= "Unknown"
                
            markAttendance(name)

            for faceloc in face_locations:    
                y1,x2,y2,x1 = faceloc
                y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(frame,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    cv2.imshow("Cam", frame)

    #end_time = time.time()

    #total_time = end_time - start_time

    #print('Time Taken : ', total_time)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
f.close