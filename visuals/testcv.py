import cv2 as cv

video_filename = 'f5_dynamic_deint_L.avi'

cap = cv.VideoCapture(video_filename)
orb = cv.ORB_create()

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print('Can\'t read frame. Exiting...')
        break
        
    kp = orb.detect(frame, None)
    kp, des = orb.compute(frame, kp)
    img = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)
    
    cv.imshow('frame', img )
    
    if cv.waitKey(25) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()