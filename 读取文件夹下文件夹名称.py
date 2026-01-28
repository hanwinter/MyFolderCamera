import os

# 要读取的文件夹路径（可以是相对路径或绝对路径）
folder_path = r'C:\Users\han90\Desktop\源文件夹'   # 修改为你的文件夹路径
output_txt = 'files.txt'

# 转为绝对路径（更稳妥）
folder_path = os.path.abspath(folder_path)

with open(output_txt, 'w', encoding='utf-8') as f:
    for name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, name)
        
        # 只写入文件，不包含子目录
        # if os.path.isfile(full_path):
        f.write(full_path + '\n')

print(f'文件绝对路径已写入 {output_txt}')
