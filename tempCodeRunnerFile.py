import numpy as np 
import cv2
import imutils
import datetime

weapon_casecade = cv2.CascadeClassifier('casecade.xml')
camera = cv2.Videocapture(0)

first_frame = None
weapon_exist = None

while True:
    ret,frame = camera.read()

    frame = imutils.resize(frame,width = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    weapon = weapon_casecade.detectMultiScale(gray,1.3 , 5, minSize = (100,100))

    if len(weapon) > 0:
        weapon_exist = True

    for(x,y,w,h) in weapon:
        frame = cv2.rextangle(frame, (x,y), (x + w, y + h),(255,0,0), 2)
        roll_gray = gray[y : y + h, x : x + w]
        roll_color = frame[y : y + h, x : x + w]
    if first_frame is None:
        first_frame = gray
        continue
    cv2.imshow("security feed",frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
if weapon_exist:
    print("Guns can Detected")
else:
    print("Guns didn't Detected")

camera.release()
cv2.destroyAllWindows()
