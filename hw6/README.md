# 개발환경 PYTHON 3.9

## 사용을 위한 실행방법

*   기본 디버깅을 통해서 실행 가능합니다.

## 소스코드 설명

*   단어 검색 프로그램
*   텍스트 파일에서 입력 단어가 몇 번 나오는지 출력
*   예) hw6.exe ../hw5/1342-0.txt PREJUDICE [Enter]
*   결과: 14를 출력

## 코드

``` python
## 오픈소스소프트웨어 2019203055 성명근 중간고사 대체 과제 hw06

intx = input('찾을 파일 txt위치 : ')

count=0 ## 중복되는 단어의 개수를 세는 변수

with open(intx,'r', encoding='UTF-8') as fr: ## with open() as문을 사용하여 txt를 r형식으로 엽니다
    
    x = input('찾는 단어 : ') ## 찾고자 하는 변수 입력

    for line in fr:
    ## fr에서 한 줄씩 뽑습니다.
        for word in line.strip().split():
            ## 한 줄을 공백으로 잘라서 for 문으로 하나씩 뽑습니다
            if x in word:
            ## 공백으로 자른 단어에 찾는 단어 x가 있다면 count를 증가해줍니다
                count+=1

print("갯수는", count) ## for문을 통해 검색한 count의 갯수를 출력합니다


```

*   찾고자 하는 단어가 들어있는 txt와 단어를 입력받을 변수와 중복되는 단어의 개수를 셀 변수를 선언합니다.
*   with open() as 문을 사용하여 열고 단어를 입력받은 후에 for문을 사용하여 한 줄씩 뽑고 뽑은거에서 
    공백으로 잘라 for문으로 하나씩 뽑습니다.
*   하나씩 뽑은 word에 x가 들어있는가를 확인하여 count를 증가시켜줍니다.
*   for문을 다 돌고 count를 출력해줍니다.