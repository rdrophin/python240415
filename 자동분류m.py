import os
import shutil

#def organize_downloads():
# 다운로드된 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더가 없으면 생성
for folder in [image_folder, data_folder, docs_folder, archive_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 파일 이동 함수 정의
def move_files(source_folder, destination_folder, extensions):
    for file in os.listdir(source_folder):
        if file.endswith(extensions):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)

# 파일 이동
move_files(download_folder, image_folder, ('.jpg', '.jpeg'))
move_files(download_folder, data_folder, ('.csv', '.xlsx'))
move_files(download_folder, docs_folder, ('.txt', '.doc', '.pdf'))
move_files(download_folder, archive_folder, ('.zip',))

print("파일 이동이 완료되었습니다.")
