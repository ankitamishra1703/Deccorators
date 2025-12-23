def dec1(func):
    def inner():
        func()
        print()
    return inner

def dec2(func):
    def inner():
        import time
        s1=time.time()       
        print(f"Started")
        func()
        s2=time.time()
        print(f"This func took {s2-s1} time to execute")
    return inner

def dec3(func):
    def inner():
        import random,time
        for i in range(5,1,-1):
            r=random.randint(1,5)
            print(r)
            i=int(input("Enter the Password:"))
            if i==r: 
                print("Loading",end='')
                for i in range(4):
                    print("..",end='')
                    time.sleep(2)
                print()       
                func()
                break
            else:
                print(f"You have more {i-1} chances")                                
                if i==r:
                    print("You have lost all your chances")
    return inner
@dec3
@dec2
@dec1
def ex():
   print("MERRY CHRISTMASS AND HAPPY NEW YEAR")
ex()
