import os
import zipfile

# 目录转zip
def zip_subfolder(parent_folder):

# parent_folder = 'D:\exam_answer_sheet_10_202412281739\\178619\\77079'

    # 判断路径是否为一个有效的文件夹路径
    if not os.path.isdir(parent_folder):
        print(f'{parent_folder}不是一个有效的文件夹路径')
        return

    # 遍历父文件夹下的所有子文件夹
    # root：当前路径
    # dirs：子文件夹路径
    # files：目录下非目录文件的名字
    for root, dirs, files in os.walk(parent_folder):
        for subdir in dirs:
            subfolder_path = os.path.join(root, subdir)
            # print(subfolder_path)
            zip_file_path = os.path.join(parent_folder, f"{subdir}.zip")
            # print(zip_file_path)
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for foldername, subfolders, filenames in os.walk(subfolder_path):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, subfolder_path)
                        zipf.write(file_path, arcname)


if __name__ == '__main__':
    parent_folder ='C:\\Users\\yibo_\\Desktop\\模拟分发上传\\英语zip\\174231\\45753'
    zip_subfolder(parent_folder)
    # print(zip_subfolder(parent_folder))
