import random,time

def guess(func):
    def inner():
        for i in range(5,1,-1):
            r=random.randint(1,5)
            print(r)
            i=int(input("Enter the no:"))
            if i==r: 
                print("Loading",end='')
                for i in range(4):
                    print("..",end='')
                    time.sleep(2)
                print()
                print("You have gussed the number correctly")              
                func()
                break
            else:
                print(f"You have more {i-1} chances")                                
                if i==r:
                    print("You have lost all your chances")
    return inner


@guess
def guss():
    
    print("MERRY CHRISTMASS")
guss()
