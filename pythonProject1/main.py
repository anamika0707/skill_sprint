import cv2

import datetime as dt


cap=cv2.VideoCapture(0)

while True:
      ret, frame = cap.read()
      date_time=str(dt.datetime.now())
      frame=cv2.putText(frame,date_time,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
      cv2.putText(frame,'ANAMIKA',(100, 80),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2,cv2.LINE_4)
      cv2.imshow("Video",frame)
      if cv2.waitKey(1)==ord("q"):
          break

cap.release()
cv2.destroyAllWindows()
