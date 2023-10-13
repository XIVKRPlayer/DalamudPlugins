import requests
import zipfile
import io
import os
import shutil
import time

print('타겟경로 : https://github.com/goatcorp/PluginDistD17')
HistoryData = input('커밋 해시 : ')

# A_Dir 디렉토리 경로
dir_path = 'plugins'
# A_Dir 디렉토리 안에 있는 파일과 디렉토리 리스트 얻기
files_and_dirs = os.listdir(dir_path)
# 디렉토리 이름들을 저장할 빈 집합 생성
Dirs = set()
# A_Dir 안의 모든 디렉토리를 Dirs 집합에 추가
for item in files_and_dirs:
    item_path = os.path.join(dir_path, item)
    if os.path.isdir(item_path):
        Dirs.add(item)

# GitHub 레포지토리 URL 및 커밋 해시 정보
github_url = 'https://github.com/goatcorp/PluginDistD17/archive/'+HistoryData+'.zip'

# GitHub URL로부터 ZIP 파일 다운로드
print(HistoryData+' 아카이브중...')
response = requests.get(github_url)

# ZIP 파일을 메모리에 저장
print(HistoryData+' 아카이브화 완료.')
zip_content = io.BytesIO(response.content)

print('오류 확인중.')
if response.status_code == 200:
    print('오류 없음.')
    time.sleep(0.1) #코드 꼬임 방지.
    zip_content = io.BytesIO(response.content)

    with zipfile.ZipFile(zip_content) as zip_ref:
        for dir_name in Dirs:
            print(dir_name+' 다운로드 완료.')
            directory_path_inside_zip = f'PluginDistD17-{HistoryData}/stable/{dir_name}'
            target_directory = os.path.join('updated_plugins', dir_name)
            os.makedirs(target_directory, exist_ok=True)  # dir_name에 해당하는 하위 폴더 생성
            
            for file_info in zip_ref.infolist():
                if file_info.filename.startswith(directory_path_inside_zip):
                    # 'PluginDistD17-...' 부분을 제외한 상대 경로를 계산하여 타겟 경로 생성
                    target_file_path = os.path.join(target_directory, os.path.relpath(file_info.filename, directory_path_inside_zip))
                    
                    if file_info.is_dir():
                        os.makedirs(target_file_path, exist_ok=True)  # 하위 디렉토리 생성
                    else:
                        with zip_ref.open(file_info) as source, open(target_file_path, 'wb') as target:
                            shutil.copyfileobj(source, target)

        print('플러그인 업데이트 완료.')
else:
    print('업데이트 파일 다운로드 실패.')