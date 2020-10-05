import cv2

faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.VideoCapture(0)

while True:
    success, vid = img.read()
    imgGray=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 8)
    for (x, y, w, h) in faces:
        cv2.rectangle(imgGray, (x, y), (x + w, y + h), (255,222, 0), 2)
    cv2.imshow("Result",imgGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



