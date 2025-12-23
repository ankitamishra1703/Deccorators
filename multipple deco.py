def dec1(func):
    def inner():
        print("Dec 1 Execution Started")
        func()
        print("Dec 1 Execution Ended")
    return inner

def dec2(func):
    def inner():
        print("Dec 2 Execution Started")
        func()
        print("Dec 2 Execution Ended")
    return inner

def dec3(func):
    def inner():
        print("Dec 3 Execution Started")
        func()
        print("Dec 3 Execution Ended")
    return inner

@dec2
@dec1
@dec3
def ex():
    print("I LOVE YOU")
ex()
