import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
width = webcam.get(cv2.CAP_PROP_FRAME_WIDTH) 
height = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT )
while True:
    _, frame = webcam.read()
    #frame = cv2.flip(frame, 1)
    gaze.refresh(frame)


    frame = gaze.annotated_frame()
    try:     
        x = gaze.horizontal_ratio()*width
        y = gaze.vertical_ratio()*height

        if gaze.is_right(): xdirection = "right" 
        if gaze.is_left(): xdirection = "left" 
        if gaze.is_center(): xdirection = "center"

        print(f"x ratio: {gaze.horizontal_ratio()},x: {x}")
        print(f"y ratio: {gaze.vertical_ratio()},y: {y}")
        cv2.circle(frame, (int(x), int(y)), 20, (255,0,0), 2)
    except:
        print("occhi non rilevati")

    cv2.imshow("Demo eye", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
