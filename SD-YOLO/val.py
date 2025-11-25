from ultralytics import YOLOv10
import os


if __name__ == '__main__':
    pt="runs/detect0/ds2_s_4696898_bs16/weights/best.pt"
    print("==================================================================")
    print(f'当前文件路径为：{pt}')
    model = YOLOv10(pt)  # load a custom model
    # Validate the model
    metrics = model.val(batch=32)  # no arguments needed, dataset and settings remembered
    map = metrics.box.map  # map50-95
    map50 = metrics.box.map50  # map50
    map75 = metrics.box.map75  # map75
    maps = metrics.box.maps  # a list contains map50-95 of each category
    print("==================================================================")
