import cv2
from ultralytics import YOLO
import datetime

try:    
    cap = cv2.VideoCapture(0) # You can use IP_Address = 'http://192.168.0.103:8080'
except:
    print("Fallo en la conexión")

# Load the model with the best-weights
model = YOLO(r'C:\Users\user\Desktop\Git-Repositories\Pothole_Detection\weights\best.pt')

class_names = ['Pothole', 'Pothole2'] 

def draw_boxes(image, boxes, class_names):
    for box in boxes:
        x1, y1, x2, y2 = box  # Coordenadas de la esquina superior izquierda (x1, y1) y la esquina inferior derecha (x2, y2)
        color = (0, 255, 0)  
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    return image

def register(quantity):
    date = datetime.datetime.now()
    if quantity != 0:
        with open("batch_register.txt", "a") as archivo:
            archivo.write(f"{date}, {quantity}\n")

while True:
    # Initialize the frame
    ret, frame = cap.read()
    # Redimensionar el frame
    resized_frame = cv2.resize(frame, (640,480))
        
    # Realizar la predicción de objetos
    result = model.predict(frame, imgsz=640, save=False)
    
    new_frame = result[0].render()
        
    cv2.imshow("Object detection", new_frame)
        
    if cv2.waitKey(1000) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

