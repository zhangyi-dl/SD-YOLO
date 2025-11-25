from ultralytics import YOLOv10
import random

model_yaml_path = "./ultralytics/cfg/models/v10/yolov10s.yaml"
# 数据集配置文件
data_yaml_path = 'dataset_1st/data/data.yaml'
# 预训练模型
pre_model_name = 'yolov10s.pt'
seed = random.randint(0, 9999999)

if __name__ == '__main__':
    # 加载预训练模型
    model = YOLOv10(model_yaml_path).load(pre_model_name)
    # 训练模型
    results = model.train(data=data_yaml_path,
                          epochs=200,
                          batch=16,
                          seed=seed,
                          name=f'ds1_s_{seed}_bs16')

