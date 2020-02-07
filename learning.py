import os
import time
#Must Access this to continue.
def main():
    while True:
        UserName = input ("Enter Username: ")
        PassWord = input ("Enter Password: ")

        if UserName == 'Vlad' and PassWord == '9188':
            time.sleep(1)
            print ("Login successful!")
            logged()

        else:
            print ("Password did not match!")

def logged():
    time.sleep(1)
    print ("Welcome to your working area")
        question = ('Would you like a coup os tea [y/n]?\n')
        print question
            while question != 'n':
                if question == 'y':
                    print('With sugar ?')
                else:
                    print("Ok")
                    time.sleep(60)
                
main()


