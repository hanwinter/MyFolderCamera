import os
import shutil

# 读取源文件夹路径
with open(r'D:\MyFolder\files.txt', 'r', encoding='utf-8') as file:
    source_folders = [line.strip() for line in file.readlines()]
# 定义目标文件夹
destination_folder = r'C:\Users\han90\Desktop\目标文件夹'  # 目标文件夹路径

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 定义图片文件的扩展名
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# 遍历源文件夹列表
for folder in source_folders:
    if os.path.exists(folder):
        for subdir, dirs, files in os.walk(folder):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in image_extensions:
                    src_file = os.path.join(subdir, file)
                    dest_file = os.path.join(destination_folder, file)

                    # 防止文件名冲突
                    counter = 1
                    while os.path.exists(dest_file):
                        base, extension = os.path.splitext(file)
                        dest_file = os.path.join(destination_folder, f"{base}_{counter}{extension}")
                        counter += 1
                    
                    # 移动文件
                    #shutil.move(src_file, dest_file)
                    #print(f"Moved: {src_file} -> {dest_file}")
                    # 复制文件
                    shutil.copy2(src_file, dest_file)
                    print(f"copy: {src_file} -> {dest_file}")
    else:
        print(f"文件夹不存在: {folder}")

print("所有图片已移动完毕！")
