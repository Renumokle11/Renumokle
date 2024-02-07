# def door(): 
#     door = input("open ")
#     print("door")
#     return
# door()



print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

def take_input():
    door = input("> ")
    return door
door = take_input()

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1.Take the cake.")
    print("2.Scream at the bear.")

    bear = input("> ")    

    if bear =="1":
        print("the beareats your face off.good job!")
    elif bear =="2":
        print("the bear eats your legs off.good job!")
    else:
        print(f"well,doing {bear} is probably better.") 
        print("bear runs away.")   

elif door == "2":
    print("you stare into the endless abyss at cthulhu's retina.")
    print("1.Blueberries.")
    print("2.yellow jacket clothespins")
    print("3.understanding revolvers yelling melodies.")

    insanity = input (">")

    if insanity=="1" or insanity=="2":
        print("your body survives powered by a mind of jello")



        