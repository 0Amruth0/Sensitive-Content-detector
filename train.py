#pip install ultralytics

from ultralytics import YOLO

model = YOLO("yolov9c.yaml")

model = YOLO("yolov9c.pt")

model.info()

results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

results = model(#path to image)
    

