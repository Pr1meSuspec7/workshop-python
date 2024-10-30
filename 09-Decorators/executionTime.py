from datetime import datetime
from time import sleep

#def executionTime(func):
#    def wrapper():
#        print('Tracking execution time...')
#        print('')
#        start = datetime.now()
#        func()
#        end = datetime.now()
#        td = (end - start).total_seconds()
#        print('')
#        print(f"Execution Time : {td:.03f}s")
#    return wrapper
#
#@executionTime

def func1():
    print('func1 execution...')
    sleep(2)

def func2():
    print('func2 execution...')
    sleep(10)

def func3():
    print('func3 execution...')
    sleep(5)


if __name__ == '__main__':
    func1()
    func2()
    func3()
