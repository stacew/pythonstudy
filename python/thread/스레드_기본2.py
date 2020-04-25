

def run(shape):
    for x in range(0, 100000):
        print(shape + ' : ' + str(x))

# # threading 보다 빠름
# run('★')
# run('◎')
# run('♡')
# run('▼')
# run('▣')
# run('◑')


# #멀티 스레드로 실행할 스레드 객체 생성, 설정

# import threading
# run1 = threading.Thread(target=run, args=('★', ))
# run2 = threading.Thread(target=run, args=('◎', ))
# run3 = threading.Thread(target=run, args=('♡', ))
# run4 = threading.Thread(target=run, args=('▼', ))
# run5 = threading.Thread(target=run, args=('▣', ))
# run6 = threading.Thread(target=run, args=('◑', ))
# #멀티 스레드 실행
# run1.start()
# run2.start()
# run3.start()
# run4.start()
# run5.start()
# run6.start()


# #이렇게 쓰면 안됨. openmp방식인가...
import  multiprocessing
pool = multiprocessing.Pool(processes=4)
pool.map(run('★'))
# pool.map(run('◎'))
# pool.map(run('♡'))
# pool.map(run('▼'))
pool.close()
pool.join()