# ATTENDANCE USING FACE RECOGNITION

The code provided is for a face recognition system that captures faces through a webcam feed, recognizes them using pre-trained face encodings, and marks attendance by writing the recognized names and timestamps to a CSV file. It uses the `face_recognition` library for face detection and recognition, OpenCV `cv2` for webcam interfacing and image manipulation, and `csv` module for logging attendance data. The attendance data is stored in CSV files named by date, making it suitable for tracking attendance over time. 

__path__ : Path where images of known faces are stored.

__csv_path__ : Path where CSV files for attendance records will be stored.

__Image File Format__ : Name.jpg (File can be of any extension)

## Installation

> git clone https://github.com/m4dhurtyagi/Attendance_Using_Face_Recogniton_In_Python.git

> cd Attendance_Using_Face_Recogniton_In_Python

> pip install -r Requirements.txt

> python Attendance_System.py

## Snapshots

![Snap](https://github.com/m4dhurtyagi/Attendance_Using_Face_Recogniton_In_Python/blob/main/assets/cam.png)

![CSV](https://github.com/m4dhurtyagi/Attendance_Using_Face_Recogniton_In_Python/blob/main/assets/att.png)
