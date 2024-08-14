from ultralytics import YOLO
import os
### Train the YOLO model on the annotated images

yolo = YOLO()






def combine_data_paths(image_path, txt_path):   
    
    images = [f for f in os.listdir(image_path) if f.endswith(".png")]
    txts = [f for f in os.listdir(txt_path) if f.endswith(".txt")]
    
    images = [f.strip(".png") for f in images]
    txts = [f.strip(".txt") for f in txts]
    
    common = list(set(images).intersection(txts))
    
    return common

    
            

def create_dataset(img_path, txt_path, train_size = 0.7, test_size= 0.15):
    common = combine_data_paths(img_path, txt_path)
    
    train_size = int(len(common) * train_size)
    test_size = int(len(common) * test_size)
    
    print(train_size, test_size)
    
    
    train = common[:train_size]
    test = common[train_size:train_size+test_size]
    val = common[train_size+test_size:]
    
    return train, test, val



def train_yolo():
    pass    


if __name__ == "__main__":
    IMAGE_DATA_PATH = "images/train"
    TXT_DATA_PATH = "ya/obj_train_data"
    
    train = create_dataset(IMAGE_DATA_PATH, TXT_DATA_PATH)
    
    
    
   