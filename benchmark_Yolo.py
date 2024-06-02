from ultralytics import YOLO
from ultralytics.utils.benchmarks import YOLO
import torch

# Cargar el modelo pre entrenado de YoLo
model = YOLO('best.pt')
# ¿Está habilitado torch el edispositivo?
print(torch.cuda.is_available())

results = model.benchmark(source="0", imgsz = 448, show = True, conf = 0.7, verbose = False, max_det = 20, iou = 0.5)

# ==== Parametro: Intersección sobre Unión (IOU) ====

#  Mide la proporción de superposición entre las predicciones del modelo 
#  y las ubicaciones reales de los objetos en una imagen, siendo una herramienta 
#  esencial para evaluar el rendimiento de modelos de detección de objetos.

# ==== Benchamarking ====

# Se refiere al proceso de evaluar y comparar el rendimiento del modelo de detección 
# de objetos utilizando métricas estándar como la precisión promedio (AP) y 
# la velocidad (FPS), generalmente en conjuntos de datos estandarizados 
# como COCO o Pascal VOC, para medir su efectividad y eficiencia en comparación
# con otros modelos similares.

#  https://docs.ultralytics.com/es/guides/yolo-performance-metrics/