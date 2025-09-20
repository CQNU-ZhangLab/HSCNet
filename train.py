import warnings, os
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/HSCNet/HSCNetn.yaml')
    model.train(data='ultralytics/cfg/datasets/VisDrone.yaml',
                batch=8,
                imgsz=640,
                patience=50,
                amp=False,
                epochs=1,
                optimizer='SGD', 
                project='runs/train',
                name='exp',
                )