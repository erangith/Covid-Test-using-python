
#Covid test using python

user_name = input("Enter your name:")

q1 = input("Do you have a fever(i.e.,chills/sweats)?(y/n):")
q2 = input("Do you have a cough(new or worsening)?(y/n):")

if (q1 == 'y' or q2 == 'y'):
    print("please", user_name, "stay home and call 811 to shedule a test.")

else:
    count = 0
    q3 = input("Do you have a headache?(y/n):")
    if (q3 == 'y'):
        count = count + 1
    q4 = input("Do you have a sore throat?(y/n):")
    if (q4 == 'y'):
        count = count + 1
    q5 = input("Do you have a runny nose / nasal congestion?(y/n):")
    if (q5 == 'y'):
        count = count + 1
    q6 = input("Do you have shortness of breath? (y/n):")
    if (q6 == 'y'):
        count = count + 1

    if (count == 1):
        print(user_name, ", you should stay home.")
    elif (count < 1):
        print(user_name, ", you should come to class.")
    else:
        print(user_name, ", you should stay home and call 811 to shedule a test.")

