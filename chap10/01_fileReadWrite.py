# file 에 white 하기 -> c 언어 읽어오기와 같은 코드 모양 // c 언어 개발자들에게 익숙한 느낌

file = open('text.txt','wt')
file.write('hello')
file.close()


# file 에 read 하기

file = open('text.txt','rt')
str = file.read()
print(str)
file.close()