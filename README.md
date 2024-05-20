# Run Yolo Model 

- **Index:**
  - Modes 
    - Train
    - Validation
    - Prediction
    - Export
    - Traking
    - Benchamarking
  - Create Environment

# Modes

![image](https://github.com/Adr4563/Object_Detection_YOLOv8/assets/135796378/076848bb-7883-4377-9932-69dd28080dcc)


## Train

Train mode se utiliza para entrenar un modelo YOLOv8 en un conjunto de datos personalizado. En este modo, el modelo se entrena utilizando el conjunto de datos y los hiperparámetros especificados. El proceso de entrenamiento implica optimizar los parámetros del modelo para que pueda predecir con precisión las clases y ubicaciones de los objetos en una imagen.

## Validation 

Validation mode se utiliza para validar un modelo YOLOv8 después de que ha sido entrenado. En este modo, el modelo se evalúa en un conjunto de validación para medir su precisión y rendimiento de generalización. Este modo se puede utilizar para ajustar los hiperparámetros del modelo para mejorar su rendimiento.

## Prediction

Predict mode se utiliza para hacer predicciones utilizando un modelo YOLOv8 entrenado en nuevas imágenes o videos. En este modo, el modelo se carga desde un archivo de punto de control, y el usuario puede proporcionar imágenes o videos para realizar inferencias. El modelo predice las clases y ubicaciones de los objetos en las imágenes o videos de entrada.

## Export

Export mode se utiliza para exportar un modelo YOLOv8 a un formato que se puede utilizar para implementarlo. En este modo, el modelo se convierte a un formato que puede ser utilizado por otras aplicaciones de software o dispositivos de hardware. Este modo es útil al implementar el modelo en entornos de producción.

## Track

Track mode se utiliza para rastrear objetos en tiempo real utilizando un modelo YOLOv8. En este modo, el modelo se carga desde un archivo de punto de control, y el usuario puede proporcionar un flujo de video en vivo para realizar el seguimiento de objetos en tiempo real. Este modo es útil para aplicaciones como sistemas de vigilancia o automóviles autónomos.

## Benchmark

Benchmark mode se utiliza para perfilar la velocidad y precisión de varios formatos de exportación para YOLOv8. Los benchmarks proporcionan información sobre el tamaño del formato exportado, sus métricas mAP50-95 (para detección de objetos, segmentación y pose) o métricas accuracy_top5 (para clasificación), y el tiempo de inferencia en milisegundos por imagen en varios formatos de exportación como ONNX, OpenVINO, TensorRT y otros. Esta información puede ayudar a los usuarios a elegir el formato de exportación óptimo para su caso de uso específico basado en sus requisitos de velocidad y precisión.


# Load the environment
First download the requierments to run code:
```
pip install -r requirements.txt
```
The requirements are: 
  - **Ultralytics**
  - **Opencv**
  - **Roboflow** 
  - **Numpy**
  - **Matplotlib**

# Object detecion

![image](https://github.com/Adr4563/Object_Detection_YOLOv8/assets/135796378/a4eff3b1-f335-4ace-9763-e70d58832967)

