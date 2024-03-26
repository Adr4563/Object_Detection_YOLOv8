import cv2
from ultralytics import YOLO
import datetime

try:    
    # IP_Address = 'http://192.168.0.103:8080'
    cap = cv2.VideoCapture(1)
except:
    print("It's doesn't to connect")

# Load the model with the best-weights
model = YOLO('C:\Users\user\Desktop\Batch\weights\best.pt')

def register(quantity):
    date = datetime.datetime.now()
    if (quantity != 0):
        with open("registro_baches.txt", "a") as archivo:
            archivo.write(f"{date}, {quantity}\n")
        
        
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Resize the frame | small frame optimise the run
    resized_frame = cv2.resize(frame, (640,480))
    
    # Display the resulting frame
    cv2.imshow("Batch-Detection", resized_frame)
        
    result = model(frame, verbose=False)
        
    if isinstance(result, list) and result:
        quantity = 0
        for item in result:
            quantity += len(item.boxes)  
            
        register(quantity)
        
    if(cv2.waitKey(30) == ord('q')):        
            break
        
cap.release()
cv2.destroyAllWindows()

