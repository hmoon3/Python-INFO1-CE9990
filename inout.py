import sys

total = 0
while True:
    lb = input("How many ladybugs are there? ")
    try:
        lb = int(lb) 
        total = total + lb
    except ValueError:
        print("BAD VALUE! EXITING NOW!!!" )
        sys.exit(1)
    print("you have ",total," so far")
