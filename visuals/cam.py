import cv2 as cv

def send_sig(send_socket, stop_flag):
    video_filename = 'f5_dynamic_deint_L.avi'
    cap = cv.VideoCapture(video_filename)

    while cap.isOpened() and not stop_flag.is_set():
        ret, frame = cap.read()
        
        if not ret:
            print('Can\'t read frame. Exiting...')
            break

        send_socket.send_data(frame)
        time.sleep(0.5)

            
        #ft = orb.detect(frame, None)
        #kp, des = orb.compute(frame, ft)
        #
        #img = cv.drawKeypoints(frame, kp, None,
        #        color=(0, 255, 0),
        #        flags=0)
        
#        cv.imshow('frame', frame)
#        
#        if cv.waitKey(25) == ord('q'):
#            break
        
#    cap.release()
#    cv.destroyAllWindows()
