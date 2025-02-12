import threading
from time import sleep

THREAD_NAME = 'THIS IS THREAD NUMBER -- # %s # --'

def countdown():
    name = threading.current_thread().name
    for i in range(10, 0, -1):
        print(name, i)
        sleep(1)
    print(name, 'BOOM!')

# Чтобы просто запустить можно сделать это одной строчкой
threading.Thread(target=countdown).start()



threads: list[threading.Thread] = []


for i in range(5):
    threads.append(threading.Thread(target=countdown, name=THREAD_NAME % i, daemon=True))
    threads[i].start()

    


for thread in threads:
    print(thread.name, 'joined')
    thread.join()
    print(thread.name, 'finished')


print('Main Thread Finished')