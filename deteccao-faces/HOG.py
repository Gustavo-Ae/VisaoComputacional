import dlib,cv2

imagem = cv2.imread(".\Images\people2.jpg")

detector_face = dlib.get_frontal_face_detector()

deteccoes = detector_face(imagem, 1) # O 1 indica a escala da imagem, muito parecido com o scaleFactor do algortimo HaarCascade

for face in deteccoes: 
    l , t , r , b = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(imagem, (l, t), (r,b), (0, 255, 255), 2)

cv2.imshow("", imagem)

cv2.waitKey(0)