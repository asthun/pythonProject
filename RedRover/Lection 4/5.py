# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает
# в качестве параметра

def benchmark(func):
    import time

    def wrapper(*arg1):
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end-start))
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')

fetch_webpage()

@benchmark
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello')