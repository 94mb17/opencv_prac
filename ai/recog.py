import face_recognition as fc
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = fc.load_image_file(os.path.join(folder,filename))
        images.append(img)
    return images

# only a file opens
face_rgb = fc.load_image_file('D:\\python_vm\\dataset\\Alexandra daddario\\Alexandra Daddario_0.jpg')

faceLoc = fc.face_locations(face_rgb)

faceLoc = faceLoc[0]

face_encode_alex = fc.face_encodings(face_rgb)[0]

face_rgb = fc.load_image_file('D:\\python_vm\\dataset\\Natalie Portman\\Natalie Portman_7.jpg')
faceLoc = fc.face_locations(face_rgb)
faceLoc = faceLoc[0]
face_encode_nat = fc.face_encodings(face_rgb)[0]

known_encodings = [face_encode_alex, face_encode_nat]
known_names = ['Alexandra Daddario', 'Natalie Portman']

f = True
count = [0, 0]

u = fc.load_image_file('D:\\python_vm\\dataset\\Natalie Portman\\Natalie Portman_76.jpg')
u = fc.face_encodings(u)[0]

images = load_images_from_folder('D:\\python_vm\\dataset\\Faces\\')

for c, i in enumerate(images):
    face_encode = fc.face_encodings(i)[0]
    itr=0
    for j in known_encodings:
        if fc.compare_faces([j], face_encode)[0]:
            count[itr] += 1
            break
        else:
            itr+=1

unknown = []

for c, i in enumerate(images):
    face_encode_not = fc.face_encodings(i)
    unknown.append(face_encode_not)

print('Alexandra Daddario: ', count[0])
print('Natalie Portman: ', count[1])