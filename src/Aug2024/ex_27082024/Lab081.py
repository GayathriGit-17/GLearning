import time

def time_decorator(func):
    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print(f"Time {end_time-start_time}")
    return wrapper()

@time_decorator
def test_ui_1():
    print("test UI1")

    test_ui_1()


