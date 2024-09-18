
while True:
    PosPoints = int(input("Possible points on assignemnt?:")) #how many points possible
    ActPoints = int(input("Points the student recived on assignment?:")) #points scored
    PercentGrade = (ActPoints / PosPoints * 100)
    if(PercentGrade > 88.999):
        print("A")
    elif(PercentGrade <= 88.999 and PercentGrade >= 74.999):
        print("B")
    elif(PercentGrade < 74.999 and PercentGrade >60.999):
        print("C")
    elif(PercentGrade <= 60.999 and PercentGrade > 50.999):
        print("D")
    else:
        print("F")




