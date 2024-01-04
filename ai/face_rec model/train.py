import os
import face_recognition as fc
import mysql.connector
import base64 as b
import numpy as np

# Training data source
folder = 'C:\\Users\\eclos\\OneDrive\\Desktop\\face'

# Database connection established and database chosen
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="faceattendence"
)

# Cursor created
cursor = mydb.cursor()

# Folder traversal for picking up data
for root, dir, file in os.walk(folder):
    for p in file:
        # Getting name
        name, ext = os.path.splitext(p)

        # Encoding
        path = os.path.join(folder, p)
        img = fc.load_image_file(path)
        face_encode = fc.face_encodings(img)[0]

        # Convert NumPy array to binary data
        face_encode_binary = face_encode.tobytes()

        # Addition in the database
        cursor.execute("INSERT INTO attendace VALUES (%s, %s)", (name, face_encode_binary))

# Committing to the database
mydb.commit()

# Closing cursor
cursor.close()

# Closing database
mydb.close()