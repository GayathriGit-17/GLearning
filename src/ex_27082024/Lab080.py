def my_decorator(func):
    # have 2 parts
    #Wrapper and call
    def wrapper():
        print("Before running UI testcase ")
        print("Start browser")
        func()
        print("Ending the UI test case")
        print("quit the browser")

        return wrapper()


@my_decorator
def test_ui():
    print("Testing UI")

    test_ui()

