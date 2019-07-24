import time, threading

WAIT_SECONDS = 5

def program():
    print("Program ran")
    threading.Timer(WAIT_SECONDS, program).start()

if __name__ == '__main__':
    program()