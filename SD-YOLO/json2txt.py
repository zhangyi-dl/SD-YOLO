import json
import os


def convert(img_size, box):
    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]

    center_x = (x1 + x2) * 0.5 / img_size[0]
    center_y = (y1 + y2) * 0.5 / img_size[1]
    w = abs((x2 - x1)) * 1.0 / img_size[0]
    h = abs((y2 - y1)) * 1.0 / img_size[1]

    return (center_x, center_y, w, h)


def decode_json(jsonfloder_path, json_name):
    txt_name = '/home/liyawei/文档/yolov10-main2/Dataset(first_time)/data/train/labels/' + json_name[0:-5] + '.txt'
    # txt保存位置

    txt_file = open(txt_name, 'w')  # te files

    json_path = os.path.join(json_folder_path, json_name)
    data = json.load(open(json_path, 'r'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']
    for i in data['shapes']:

        if (i['shape_type'] == 'rectangle'):  # 仅适用矩形框标注

            x1 = float(i['points'][0][0])
            y1 = float(i['points'][0][1])
            x2 = float(i['points'][1][0])
            y2 = float(i['points'][1][1])
            if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
                continue
            else:
                bb = (x1, y1, x2, y2)
                bbox = convert((img_w, img_h), bb)
            if i['label'] == "0":
                txt_file.write("0 " + " ".join([str(a) for a in bbox]) + '\n')
            elif i['label'] == "1":
                txt_file.write("1 " + " ".join([str(a) for a in bbox]) + '\n')
            elif i['label'] == "2":
                txt_file.write("2 " + " ".join([str(a) for a in bbox]) + '\n')
            elif i['label'] == "3":
                txt_file.write("3 " + " ".join([str(a) for a in bbox]) + '\n')
            elif i['label'] == "4":
                txt_file.write("4 " + " ".join([str(a) for a in bbox]) + '\n')



if __name__ == "__main__":

    json_folder_path = '/home/liyawei/文档/yolov10-main2/Dataset(first_time)/data/train/labels_json'  # json文件夹路径
    json_names = os.listdir(json_folder_path)  # file name
    for json_name in json_names:  # output all files
        if json_name[-5:] == '.json':  # just work for json files
            decode_json(json_folder_path, json_name)
