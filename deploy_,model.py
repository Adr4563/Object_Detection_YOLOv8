import cv2
from ultralytics import YOLO
import datetime

try:    
    # IP_Address = 'http://192.168.0.103:8080'
    cap = cv2.VideoCapture(0)
except:
    print("Fail conection")

# Load the model with the best-weights
model = YOLO(r'C:\Users\user\Desktop\Git-Repositories\Pothole_Detection\weights\best.pt')

def register(quantity):
    date = datetime.datetime.now()
    if (quantity != 0):
        with open("batch_register.txt", "a") as archivo:
            archivo.write(f"{date}, {quantity}\n")
        
        
while True:
    # Initialize capture
    ret, frame = cap.read()
    # Resize the frame
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

