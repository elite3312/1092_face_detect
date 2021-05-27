import cv2
def main(name):
  cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
  cap.set(cv2. CAP_PROP_FRAME_WIDTH, 320)
  cap.set(cv2. CAP_PROP_FRAME_HEIGHT, 240)
  #variable to record this is the nth picture taken
  pictureCount=0

  while(cap.isOpened()):
    # get a frame
    ret, frame = cap.read()
      
    cv2.imshow("press c to capture, then press q to finish", frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
      cv2.putText(frame, 'Smile', (200, 200), cv2. FONT_HERSHEY_SIMPLEX , 2, ( 255, 255, 255), 2, cv2. LINE_AA)          
      cv2.imshow( "press c to capture, then press q to finish", frame)
      cv2.waitKey(1000)
      ret, frame = cap.read()
      cv2.imwrite("rec/pic/"+name+"#"+str(pictureCount)+".jpg", frame)
      cv2.putText(frame, 'ok', (200, 250), cv2. FONT_HERSHEY_SIMPLEX , 2, ( 255, 255, 255), 2, cv2. LINE_AA)          
      cv2.imshow( "press c to capture, then press q to finish", frame)
      cv2.waitKey(300)
      pictureCount+=1
      if(pictureCount>=3):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  
      
  cap.release()
  cv2.destroyAllWindows()

