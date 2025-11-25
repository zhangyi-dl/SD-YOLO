import os

# 定义原始字符和替换字符
original_str = "lose"
replacement_str = "2"

# 指定存放txt文件的目录路径
folder_path = "./1"

# 获取目录下所有txt文件的文件名列表
file_names = os.listdir(folder_path)

# 循环遍历每个txt文件，并替换其中的字符
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "r") as file:
        content = file.read()
    # 替换字符
    new_content = content.replace(original_str, replacement_str)
    # 将替换后的内容写回文件
    with open(file_path, "w") as file:
        file.write(new_content)

print("Replacement completed!")