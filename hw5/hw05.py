## 오픈소스소프트웨어 2019203055 성명근 중간고사 대체 과제 hw05

import requests ## requests 모듈 사용

url = input('다운 받고자 하는 URL : ') ## URL입력

r = requests.get(url, allow_redirects=True)  ## get메소드 사용

open('1342-0.txt', 'wb').write(r.content.upper())
## 파일을 wb로 열고 r.content를 대문자로 1342-0.txt에 저장한다
