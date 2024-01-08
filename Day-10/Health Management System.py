""" Health Management System
3 clients - Prabin Saugat Pragyan
def getdate():
import datetime
return datetime.datetime.now()

total 6 files
write a function that when executes takes as input client name
fuunction for diet or exercise

"""
def getdate():
    import datetime
    return datetime.datetime.now()

def log(q):
    if (q == 1):
        print("What do you want of Prabin's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            print("ADD Diet Here")
            u = input()
            with open("prabin-food.txt","a") as p:
                p.write(str([str(getdate())])+ ":"+ u )
                print("Successfully Written")
        else:
            print("ADD Exercise Here")
            u = input()
            with open("prabin-exercise.txt","a") as p:
                p.write(str([str(getdate())])+ ":" + u )
                print("Succesfully Written")
    elif (q == 2):
        print("What do you want of Saugat's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            print("ADD Diet Here")
            u = input()
            with open("saugat-food.txt","a") as p:
                p.write(str([str(getdate())])+ ":"+ u )
                print("Successfully Written")
        else:
            print("ADD Exercise Here")
            u = input()
            with open("saugat-exercise.txt","a") as p:
                p.write(str([str(getdate())])+ ":" + u)
                print("Successfully Written")
    else:
        print("What do you want of Pragyan's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            print("ADD Diet Here")
            u = input()
            with open("pragyan-food.txt","a") as p:
                p.write(str([str(getdate())])+ ":"+ u )
                print("Successfully Written")
        else:
            print("ADD Exercise Here")
            u = input()
            with open("pragyan-exercise.txt","a") as p:
                p.write(str([str(getdate())])+ ":" + u )
                print("Successfully Written")

def retrieve(q):
    if (q == 1):
        print("What do you want to retrieve of Prabin's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            with open("prabin-food.txt") as p:
                i = p.readlines()
                print(i)
        else:
            with open("prabin-exercise.txt") as p:
                i = p.readlines()
                print(i)
    elif (q == 2):
        print("What do you want of Saugat's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            with open("saugat-food.txt") as p:
                i = p.readlines()
                print(i)
        else:
            with open("saugat-exercise.txt") as p:
                i = p.readlines()
                print(i)

    else:
        print("What do you want of Pragyan's?")
        print("Press 1 for Diet "
              "Press 2 for Exercise")
        o = int(input())
        if (o == 1):
            with open("pragyan-food.txt") as p:
                i = p.readlines()
                print(i)
        else:
            with open("pragyan-exercise.txt") as p:
                i = p.readlines()
                print(i)

print("HEALTH MANAGEMENT SYSTEM")
print("You want to log or retrieve the data?")
print("Press '1' to log or press '2' to retrieve")
p = int(input())
if(p==1):
    print("Whose Data you want to Log?")
    print("Press 1 for Prabin's "
          "Press 2 for Saugat's"
          "Press 3 for Pragyan's")
    q = int(input())
    log(q)

else:
    print("Whose Data you want to Retrieve?")
    print("Press 1 for Prabin's "
          "Press 2 for Saugat's"
          "Press 3 for Pragyan's")
    q = int(input())
    retrieve(q)


