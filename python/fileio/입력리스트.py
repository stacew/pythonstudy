movies = []

for i in range(0, 3):
    data = input('영화 제목 입력 >> ')
    movies.append(data)

print(movies)

#파일로 저장해봅시다.
file = open('fileio/movies.txt','w')

for i in range(0, len(movies)):
    file.write(movies[i] + '\n')

file.close()

#UTF-8로 file 저장하려면 사용
import codecs 
with codecs.open('fileio/movies2.txt','w', "utf-8") as file2: #python 로컬 빠져 나가면 자동으로 닫아지는 방법.
   
    #하지 말라고 함.
    # #file2.write(codecs.BOM_UTF8)
    #file2.write(u'\ufeff')

    for i in range(0, len(movies)):
        file2.write(movies[i] + '\n')
