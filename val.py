import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('best.pt')
    result = model.val(data='ultralytics/cfg/datasets/VisDrone.yaml', imgsz=1024, split='val', project='runs/val', name='exp')