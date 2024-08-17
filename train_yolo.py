from ultralytics import YOLO
import os
### Train the YOLO model on the annotated images
def combine_data_paths(image_path, txt_path):
    image_files = os.listdir(image_path)
    txt_files = os.listdir(txt_path)
    
    combined_data = []
    for image_file in image_files:
        for txt_file in txt_files:
            if image_file.split(".")[0] == txt_file.split(".")[0]:
                combined_data.append((f"{image_path}/{image_file}", f"{txt_path}/{txt_file}"))
    return combined_data


def test_yolo( model_path = "pdf_reader2/weights/best.pt", source="images/test"):
    
    
    if os.path.exists(model_path):
        print("Model exists")
    
    
    for img in os.listdir(source):
        yolo_model = YOLO(model_path)
        results = yolo_model(
            source=f"{source}/{img}",
            conf = 0.5,
            show = True
            
        )


        
def train():
    # Initialize the YOLOv8 model (use the model name or model file)
    yolo_model = YOLO("yolov8n.yaml")  # or "yolov8s.pt" depending on the model you want

    # Train the model with a custom output model name
    yolo_model.train(data="config/config.yaml", epochs=100, name="pdf_reader")

if __name__ == "__main__":  
    test_yolo()