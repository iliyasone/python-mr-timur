from threading import Thread
from time import sleep, time


def loading_status_bar(workload_thread: Thread):
    current_text = ''
    while workload_thread.is_alive():
        current_text += '■'
        print(current_text)
        if len(current_text) > 4:
            current_text = ''
        sleep(1)


def workload_function():
    sleep(11.5)
    print('MAIN THREAD DONE')

def start_workload():
    working_thread = Thread(target=workload_function)
    status_thread = Thread(target=loading_status_bar, args=(working_thread,))

    working_thread.start()
    status_thread.start()

start_workload()