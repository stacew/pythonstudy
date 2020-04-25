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