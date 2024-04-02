from ultralytics import YOLO
import cv2
import numpy as np
from sort import Sort

cap = cv2.VideoCapture(0) 

model = YOLO("yolov8n.pt")

# Initializie the tracker: Bot_SORT & ByteTrack
tracker = Sort()

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    
    # Resized the frame: 
    # Itarator frames
    results = model.track(frame, stream=True)
    
    for res in results:
        # print(res.boxes)
        # Print atributes: clss, conf, shapes  (xywh, xywhn, xyxy,etc.) 
        
        conf = (res.boxes.conf.cpu().numpy())[0]
        
        if( conf > 0.4 and conf !=None):
            # print( "The conf default ", res.boxes.conf )
            # print( "ID default", res.boxes.id )
            boxes = res.boxes.xyxy.cpu().numpy().astype(int)
        
            tracks = tracker.update(boxes).astype(int)
            # print(tracks)
            # numpy: [xmin, ymin, xmax, ymax, track_id]
        
            for xmin, ymin, xmax, ymax, track_id in tracks:
                # Write Text
                cv2.putText(img=frame, text=f"-{track_id}-{conf:.2f}", org=(xmin, ymin-10), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255,0,0), thickness=2)
                # Draw the boxxes
                cv2.rectangle(img=frame, pt1=(xmin, ymin), pt2=(xmax, ymax), color=(0, 0, 255), thickness=2)             

        # annotations = results[0].plot()
    
    cv2.imshow("YOLOv8 Tracking", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# References
# 
# https://github.com/freedomwebtech/yolov8counting-trackingvehicles
# Track & Count Objects using YOLOv8 ByteTrack & Supervision
#
# https://www.youtube.com/watch?v=OS5qI9YBkfk&t=453s
# 

