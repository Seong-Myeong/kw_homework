# 개발환경 PYTHON 3.9 ( requests 모듈 사용 )

## 사용을 위한 실행방법

*   python에 requests모듈이 깔려있어야 소스코드를 사용가능하다. 
*   pip install requests를 사용하여 모듈을 설치해야한다.

## 소스코드 설명

*   영문 웹문서 다운로드 프로그램
*   URL로 주어진 문서를 모두 대문자로 저장
*   예) hw5.exe www.gutenberg.org/files/1342/1342-0.txt [Enter]
*   결과: 1342-0.txt (대문자로만 저장된 텍스트 파일) 생성
*   소문자만 대문자로 바꿔주면 됨

## 코드

``` python

## 오픈소스소프트웨어 2019203055 성명근 중간고사 대체 과제 hw05

import requests ## requests 모듈 사용

url = input('다운 받고자 하는 URL : ') ## URL입력

r = requests.get(url, allow_redirects=True)  ## get메소드 사용

open('1342-0.txt', 'wb').write(r.content.upper())
## 파일을 wb로 열고 r.content를 대문자로 1342-0.txt에 저장한다


```

*   requests 모듈을 사용합니다.
*   url 변수를 만들어 다운로드할 URL을 입력받습니다.
*   get 메소드를 사용하여 리다이렉션하여 r에 저장합니다.
*   open을 사용하여 1342-0.txt를 wb로 생성하고 r의 내용을 대문자로 저장합니다.