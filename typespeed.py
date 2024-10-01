import random as rn
from time import time

def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_test(time_s, time_e, userinput):
    time_diff = time_e - time_s
    time_r = round(time_diff, 2)
    words = len(userinput.split())
    wpm = (words / time_r) * 60
    return round(wpm)

if __name__ == '__main__':
    while True:
        check = input("Ready for test: Yes/No : ").strip().capitalize()
        if check == "Yes":
            test = [
                "My name is Likitha. I love to travel to LADAKH. The beauty of Ladakh lies in peaks of the Himalayas, the golden sand dunes of Nubra Valley, and the waters of Pangong Tso, creating an inspiring  of nature’s artistry."
            ]

            test1 = rn.choice(test)

            print("\n****************** Typing Speed Calculator ******************\n")
            print(test1)
            print("\nStart typing after pressing Enter...\n")
            
            time_1 = time()
            testinput = input("Enter: ")
            time_2 = time()
        
            print("\nResults:")
            print("Speed:", speed_test(time_1, time_2, testinput), "wpm")
            print("Errors:", mistake(test1, testinput))

        elif check == "No":
            print("Thank you!")
            break
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")
