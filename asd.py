import cv2
from ultralytics import YOLO

# Cargar el modelo YOLOv8 y sus pesos
model = YOLO(r'C:\Users\user\Desktop\Git-Repositories\Pothole_Detection\weights\best.pt')

# Cargar los nombres de las clases (si están disponibles)
class_names = ["Pothole"] 

def draw_boxes(image, boxes, class_names):
    for box in boxes:
        x1, y1, x2, y2 = box  # Coordenadas de la esquina superior izquierda (x1, y1) y la esquina inferior derecha (x2, y2)
        color = (354, 255, 0)  # Color verde
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    return image

# Iniciar captura de video desde la cámara
cap = cv2.VideoCapture(0)  

while True:
    # Capturar un frame de la cámara
    ret, frame = cap.read()

    # Realizar la detección de objetos con YOLOv8
    detections = model.predict(frame, imgsz = 640, conf = 0.4)

    # Verificar si las detecciones son válidas y si tienen cajas delimitadoras
    if isinstance(detections, list):
        None
    elif detections.xyxy:
        boxes = detections.xyxy[0]  # Format [x_min, y_min, x_max, y_max]
        frame = draw_boxes(frame, boxes, class_names)
        
    
    new_frame = detections[0].plot()

    cv2.imshow('Object Detection', new_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos y cerrar ventanas
cap.release()
cv2.destroyAllWindows()

