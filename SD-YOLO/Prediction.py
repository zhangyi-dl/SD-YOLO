from ultralytics import YOLOv10
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
model = YOLOv10('best.pt')
results = model.predict("dataset_2st/data/train/images/00087-3547249623.png")
# Display the results
results[0].show()


