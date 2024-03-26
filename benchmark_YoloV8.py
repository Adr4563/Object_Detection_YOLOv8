from ultralytics import YOLO
from ultralytics.utils.benchmarks import YOLO
import torch

model = YOLO('best.pt')
print(torch.cuda.is_available())

results = model.benchmark(source="0", imgsz = 448, show = True, conf = 0.7, verbose = False, max_det = 20, iou = 0.5)

# ==== Parametro: Intersección sobre Unión (IOU) ====

#  Mide la proporción de superposición entre las predicciones del modelo 
#  y las ubicaciones reales de los objetos en una imagen, siendo una herramienta 
#  esencial para evaluar el rendimiento de modelos de detección de objetos.

# ==== Benchamarking ====

#  Práctica de medir y evaluar el rendimiento de un sistema, modelo o algoritmo 
#  comparándolo en términos de velocidad y precisión en la detección de objetos.
#  Asimismo evaluación del Consumo de Recursos utlizados por el modelo con respecto
#  a la cantidad de memoria RAM, el uso de la CPU o GPU, etc.

#  https://docs.ultralytics.com/es/guides/yolo-performance-metrics/
