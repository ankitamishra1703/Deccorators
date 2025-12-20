import random,time

def guess(func):
    def inner():
        n=6
        for i in range(1,n):
            r=random.randint(1,9)
            print(r)
            i=int(input("Enter the no:"))
            if i==r: 
                for i in range(4):
                    time.sleep(2)              
                func()
                break
            else:
                print(f"You have more {n-2} chances")
                n-=1                
                if i==5:
                    print("You have lost all your chances")
    return inner


@guess
def guss():
    print("You have gussed the number correctly")
guss()
