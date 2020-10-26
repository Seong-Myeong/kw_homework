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
