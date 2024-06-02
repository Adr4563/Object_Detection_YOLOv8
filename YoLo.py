from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0) 

model = YOLO("yolov8n.pt")

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    
    results = model.predict(frame, persist=True)
    # Tracking
    # results = modelo.track(frame, persist=True)

    annotations = results[0].plot()
    
    cv2.imshow("YOLOv8 Tracking", annotations)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()