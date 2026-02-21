# maths=int(input("enter maths marks:"))
# science=int(input("enter science marks:"))
# english=int(input("enter english marks:"))

# total_percentage=((maths+science+english)/300)*(100)
# if(total_percentage>40 and maths>33 and science>33 and english>33):
#     print("congrats you are pass",total_percentage)
# else:
#     print("you are fail better luck next time",total_percentage)
# p1 = "subscribe now"
# p2 = "buy now"
# p3 = "make lot of money"
# p4 = "want to win iphone"

# message = input("enter comment: ")

# if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
#     print("this is spam")
# else:
#     print("this is genuine")
# username=input("enter name:")
# if(len(username)>10):
#     print("this is invalid username")
# else:
#     print("your username is valid")
# l=["dev","rohan","nilesh","harsh"]
# name=input("enter name: ")
# if(name in l):
#     print("your name is in list")
# else:
#     print("your name is not in list")
marks=int(input("enter your marks: "))
if(marks<=100 and marks>=90):
    grade="ex"
elif(marks<90 and marks>=80):
    grade="a"
elif(marks<80 and marks>=70):
    grade="b"
elif(marks<70 and marks>=60):
    grade="c"
elif(marks<60 and marks>=50):
    grade="d"
elif(marks<50 and marks>=40):
    grade="f"
print("your grade is ",grade)