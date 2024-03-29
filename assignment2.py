# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import sys
import argparse


class Assignment2:
    age = 0
    birthYear = ""
    n = 0
    host = ""


    # Task 1 (Constructor)

    def __init__(self, age=0):
        self.age = age

    # Task 2 (birthYear)

    def tellBirthYear(self, currentYear=0):

        number = currentYear - self.age
        self.birthYear = str(number)
        print("Your birth year is {0}".format(self.birthYear))

    # Task 3 (List)

    def listAnniversaries(self, n=0):

        result_list = []
        aniversary = 1

        while aniversary <= self.age:
            if aniversary % n == 0:
                result_list.append(aniversary)
            aniversary = aniversary + 1

        return result_list

    # Task 4 (String Manipulation)

    def modifyAge(self, n=0):

        pos = 0
        stringAge = str(self.age)
        stringNth = str(self.age ** n)
        returnString = str(n * self.age)

        while pos < n:
            returnString = returnString + stringAge[0]
            pos = pos + 1

        pos = 0
        while pos <= len(stringNth):
            if pos % 2 != 0:
                returnString = returnString + stringNth[pos - 1]
            pos = pos + 1

        return returnString

    # Task 5 (Loop and Conditional statements)
    @staticmethod
    def checkGoodString(string=""):

        if len(string) < 9:
            return False
        elif not str(string[0]).islower():
            return False
        pos = 0

        while pos < len(string):
            if str(string[pos]).isdigit():
                return True
            pos = pos + 1
        return False

    # Task 6 (Socket)
    @staticmethod
    def connectTcp(host="", port=0):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            host = socket.gethostbyname(host)
            print("Good Host")
        except:
            print("Could not connect to host")
            return False
        try:
            sock.connect((host, port))
            return True
        except socket.error:
            return False

        self.sock.close()


print("Task 5")
ret = Assignment2.checkGoodString("Foobar0more")
print(ret)

ret = Assignment2.checkGoodString("foobar0more")
print(ret)

print("Task 6")
retval = Assignment2.connectTcp("www.google.com", 80)

if retval:
    print("Connection established correctly")
else:
    print("Some error")

print(retval)
