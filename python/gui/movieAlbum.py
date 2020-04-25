import tkinter

#이미지 정보에 대한 리스트를 만들어주자
img = ['gui/file/1.png','gui/file/2.png','gui/file/3.png','gui/file/4.png','gui/file/5.png']
title = ['1917','엽문','주디','오픈더도어','n번째이별중']
rates = [17.11, 12.21, 10.19, 9.24, 6.82]
index = 2 #시작 위치

def setAlbum(increase):
    # global을 안 적으면, 외부 값 세팅하고, 그 뒤로 다른 곳(스레드 이용)에서 변경돼도 처음 이 함수 내에서는 처음 값 그대로 씀.
    global index 
    
    index += increase
    index %= 5

    print('영화명 : ' + title[index])
    print('예매율 : ' + str(rates[index]) + '%\n')

    newPhoto = tkinter.PhotoImage(file=img[index])
    btn.configure(image=newPhoto)
    btn.image = newPhoto

def prevCall():
    setAlbum(-1)

def postCall():
    setAlbum(+1)


frame = tkinter.Tk() #부품을 복사해서 가지고 왔음. (Tk <- 대문자로 된 건 복사해서 쓴다.)

#이전 버튼 만들어서 넣음.
prev = tkinter.Button(frame, text='<< 이전으로', command=prevCall)#command는 클릭 이벤트
prev.pack()

# 이미지 들어가는 부분
btn = tkinter.Button(frame) # 버튼이 들어갈 자리는 frame이라고 설정
btn.pack() #++++++ frame에 등록..??

setAlbum(0)

#이후 버튼 만들어서 넣음.
post = tkinter.Button(frame, text='>> 이후로', command=postCall)
post.pack()


frame.mainloop() #프레임을 계속 떠 있게 함.