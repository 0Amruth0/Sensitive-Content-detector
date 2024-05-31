from ultralytics import YOLO
import cv2
import numpy as np

# Load model
model = YOLO("yolov9c.pt")  # Load your trained model

# Image path
image_path = "path/to/your/image.jpg"

# Perform inference
results = model(image_path)  # Predict on image

# Get the first result (assuming a single image)
result = results[0]

# Iterate through detected objects
for box in result.boxes:
    # Extract coordinates
    x1, y1, x2, y2 = box.xyxy[0].tolist() 

    # Convert to integer (for drawing)
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Get class label and confidence
    class_id = box.cls[0]
    confidence = box.conf[0]

    # Draw bounding box on image
    class_name = model.names[int(class_id)]
    label = f"{class_name} {confidence:.2f}"

    # Read image for OpenCV
    img = cv2.imread(image_path)

    # Draw rectangle and label on image
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2) # Green rectangle
    cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the resulting image
cv2.imshow("Detected Objects", img)
cv2.waitKey(0)
