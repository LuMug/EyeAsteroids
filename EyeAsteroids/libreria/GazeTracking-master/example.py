import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
width = webcam.get(cv2.CAP_PROP_FRAME_WIDTH) 
height = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT )

while True:
    _, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    gaze.refresh(frame)


    frame = gaze.annotated_frame()
    try:
        #left_pupil = str(gaze.pupil_left_coords())
        #right_pupil = str(gaze.pupil_right_coords())
        #left_pupil =left_pupil[1:-1]
        #right_pupil=right_pupil[1:-1]

        #array_left_pupil =left_pupil.split(",")
        #array_right_pupil=right_pupil.split(",")

        # center_y= (int(array_left_pupil[1].strip())+int(array_right_pupil[1].strip()))/2
        #center_x= (int(array_left_pupil[0].strip())+int(array_right_pupil[0].strip()))/2

        
        x = (gaze.horizontal_ratio())*width
        y =(gaze.vertical_ratio())*height
        print("x" +str(x))
        print("y" + str(y))
        cv2.circle(frame, (int(x), int(y)), 20, (255,0,0), 2)
        cv2.putText(frame, "ratio x" + str(gaze.horizontal_ratio()), (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "ratio y" + str(gaze.vertical_ratio()), (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    except:
        print("occhi non rilevati")

    cv2.imshow("Demo eye", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()