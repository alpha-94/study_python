with open('text.txt','rt') as file: # 파이썬은 이렇게 코드 작성
    str = file.read()
    print(str)
    #file.close() # with 사용 시 close 코드 필요 X


'''
# 텍스트 파일 읽기 / 쓰기
    1. 문자열을 담은 리스트를 파일에 쓰는 writelines() 메서드

'''


# ex1 )
lines = ['we`ll find a way ew always have - Intersteller\n',
         'I`ll find you and I`ll kill you - Taken\n',
         'I`ll be back - Terminator2\n']

with open('movie_quotes.txt','w') as file:
    for line in lines:
        file.write(line)


# ex2 )
with open('movie_quotes.txt','w') as file:
    file.writelines(lines)
    
'''
# 텍스트 파일 읽기 / 쓰기
    2. 줄단위로 텍스트를 읽는 readline() & readlines() 메서드

'''

# ex1 )
with open('movie_quotes.txt','r') as file:
    line = file.readline()

    while line != '':
        print(line,end='')
        line = file.readline()


# ex2 )
with open('movie_quotes.txt','r') as file: # 퍼포먼스가 이게 더 좋음
    lines = file.readlines()
    line = ''
    for line in lines:
        print(line,end='')
















