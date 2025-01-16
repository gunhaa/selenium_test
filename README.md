
```shell
# 가상환경 라이브러리 가져오기
`pip install virtualenv`

# 리스트 확인
pip list

# 가상환경 생성
# 생성할 폴더로 이동후
# foldername에는 폴더명을 입력
# 관행상 venv로 많이 만든다
python -m virtualenv ${folderName}

# 에러 발생시 powershell에서
set-executionpolicy unrestricted
# 입력 후, a로 모두 예 로 설정 활성화

# 가상환경 활성화
.\folder\Scripts\activate

# 가상환경 비활성화
deactivate

# 가상환경 활성화 후
pip install selenium chromedriver_autoinstaller

# 가상환경 세팅 내보내기
pip freeze > requirements.txt

# 가상환경 가져오기
pip install -r requirements.txt
```