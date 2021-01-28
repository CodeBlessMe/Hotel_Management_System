import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from AccountClasses import *


# now, except the track function is not finished, other functions are worked

# Welcome to app
def welcome():
    print("*******************\nWelcom to Accountbook App")
    print("*******************\n")


# prompt user whether already have account
def prompt():
    prompt = input("Do you already have an account?\n You can type Y(yes) or N(no):")
    # log in according to Y or N
    # If not Y or N, input again
    while prompt != '':
        if (prompt != 'N' and prompt != 'Y'):
            prompt = input("Please input Y or N:")
        else:
            break
    # If you don't have account, please create one
    if prompt == 'N':
        user = input("You can create a new account here, \nplease create your username:")
        pswd = input("Please create your password here:")
        # add created user into users array
        users.append([user, pswd])
        print("Create new account successfully! ")
        print(users)
    # If you already have account,please log in
    elif prompt == 'Y':
        user = input("Please input your username:")
        pswd = input("Please input your password:")
        # Judge whether inputted user and password in users array
        while user != "" and pswd != "":
            # use built-in any to judge
            a = any(user in i[0] and pswd in i[1] for i in users)
            # print(a)
            if a == True:
                break
            else:  # if not in users,namely wrong username or wrong password, input again
                user = input("Please input a correct username:")
                pswd = input("Please input a correct password:")
        print("Log in successfully!")  # if username and password correct, break there
    return user  # return username to prompt()


# We already got a username via prompt(),then create an instance named by the username
def trans_username_wallet():
    a = get_user + 'wallet'
    a = wallet()
    return a


# greeting at first
def begin():
    print('Hello, ' + get_user + '! This is your powerful wallet.')
    print('Now! Let\'s start!')


# read local data file
def openfile():
    if (os.path.exists('D:\学习\VUB课程\Advanced Programming Concepts\Project\APCproject\\' + get_user + 'data.txt') != 0):  # #if there is the data file
        file = open('D:\学习\VUB课程\Advanced Programming Concepts\Project\APCproject\\' + get_user + 'data.txt', 'r')
        s = file.read()
        s = s.split(';')
        olddata = []
        for i in s[:-1]:
            i = i.split(',')
            category = []
            category.append(i[0])
            count = 0
            expense = []
            for j in i[1:-1]:
                if (count == 0):
                    expense.append(float(j))
                    count += 1
                else:
                    expense.append(j)
                    category.append(expense)
                    expense = []
                    count = 0
            olddata.append(category)
        return olddata


# default categories in local userdata file
def defaultcategories():
    if (os.path.exists('D:\学习\VUB课程\Advanced Programming Concepts\Project\APCproject\\' + get_user + 'data.txt') != 0):
        mywallet.data = openfile()
    else:  # build a wallet and several default categories firstly
        mywallet.addcategory('Shop')
        mywallet.addcategory('Transport')
        mywallet.addcategory('General')


# an input function
def inputchoice():
    response = int(input())
    return response


# ask users to select from add, track delete or quit
def get_choice_1():
    print('What do you want to do?')
    print('1.Add        2.Track        3.Delete')
    print('  4.Back to login           5.Quit')
    response = inputchoice()
    while (response < 1) or (response > 5):
        print('Please enter right number.')
        response = inputchoice()
    return response


# print all created categories for choosing
def printcategoryories():
    count = 2
    for i in mywallet.data:
        print(count, '.', i[0])
        count += 1


# ask about what category want to add to
def get_choice_2():
    print('Which category do you want to add to?')
    print('1 . Create new catogory')
    printcategoryories()
    response = inputchoice()
    while (response > len(mywallet.data) + 1) or (response < 1):
        print('Please enter right number: ')
        response = inputchoice()
    return response


# create a new category
def create_category():
    name = input('Please enter its name: ')
    mywallet.addcategory(name)


# add a new expense
def addexpense(choice):
    payment = float(input('Please enter payment: '))
    text = input('Do you want to write note?')
    newexpense = expense(payment, text)
    mywallet.addexpense(choice - 2, newexpense.dataexpense)


# ask users want to track details or by categories(Sector diagram)
def get_choice_3():
    print('Do you want to track by categories or the distribution?')
    print('1.By categories   2.The distribution')
    response = inputchoice()
    while (response < 1) or (response > 2):
        print('Please enter right number.')
        response = inputchoice()
    return response


# after users answer showing detail, let users choose a category or all
def get_choice_4():
    print('Which category do you want to show?')
    print('1 . All catogories')
    printcategoryories()
    response = inputchoice()
    while (response > len(mywallet.data) + 1) or (response < 1):
        print('Please enter right number: ')
        response = inputchoice()
    return response


##after users choose to show all category, show all expenses
def showallcategory():
    for i in mywallet.data:
        print(i[0])
        for j in i[1:]:
            print(j[0], j[1])


# after users choose to show a category, show all expenses in this category
def showcategory(category):
    print(mywallet.data[category - 2][0])
    for i in mywallet.data[category - 2][1:]:
        print(i[0], i[1])


def showdistribution():
    sums = []
    labels = []
    for i in mywallet.data:
        sum = 0
        for j in i[1:]:
            sum += j[0]
        if (sum != 0):
            sums.append(sum)
            labels.append(i[0])
    plt.figure()
    plt.pie(sums, labels=labels, autopct='%1.1f%%')
    plt.title("The distribution of payment")
    plt.show()



# ask users want to delete a category or a expense
def get_choice_5():
    print('What do you want to delete? ')
    print('1.Category  2.Expense')
    response = inputchoice()
    while (response < 1) or (response > 2):
        print('Please enter right number.')
        response = inputchoice()
    return response


# delete a category
def deletecategory():
    name = input('Please enter the name of category: ')
    mywallet.deletecategory(name)


# delete a expense
def deleteexpense():
    payment = float(input('Please enter the payment of expense: '))
    note = input('Please enter the note of expense: ')
    mywallet.deleteexpense(payment, note)


# store new data to file
def store(data):
    file = open('D:\学习\VUB课程\Advanced Programming Concepts\Project\APCproject\\' + get_user + 'data.txt', 'w')
    s = ''
    for category in data:
        s = s + category[0] + ','
        for i in category[1:]:
            s = s + str(i[0]) + ',' + str(i[1]) + ','
        s = s + ';'
    file.write(s)
    file.close()


# ******************************************************************
# the following is the executing program

# welcome interface
welcome()
# default accountbook users and their passwords, if one create new account, the infos will be included
users = [['Tom', '123'], ['Jerry', '456']]

# Login interface, ask whether you have account
get_user = prompt()
# assign the instance named by username to mywallet
# That is to say when an account is logged in, his or her own accountbook will be created
mywallet = trans_username_wallet()
# default categories in local file
defaultcategories()

begin()
choice_1 = get_choice_1()  # ask users to select from add, track delete, back to log in or quit

while (choice_1 != 5):  # if choice_1 = 5, quit
    if (choice_1 == 1):  # choose to add
        choice_2 = get_choice_2()
        if (choice_2 == 1):  # add a category
            create_category()
        else:  # add an expense
            addexpense(choice_2)
    elif (choice_1 == 2):  # choose to track
        choice_3 = get_choice_3()
        if (choice_3 == 1):  # track details
            choice_4 = get_choice_4()
            if (choice_4 == 1):
                showallcategory();
            else:
                showcategory(choice_4)
        else:  # track by categories
            showdistribution();
    elif (choice_1 == 3):
        choice_5 = get_choice_5()  # choose to delete
        if (choice_5 == 1):  # delete a category
            deletecategory()
        else:  # delete a expense
            deleteexpense()
    else:
        store(mywallet.data)  # before relogin, store last one's wallet data
        welcome()  # back to welcome interface and login
        get_user = prompt()  # reget user infos
        mywallet = trans_username_wallet()
        defaultcategories()
        begin()
    choice_1 = get_choice_1()  # repeat the loop
store(mywallet.data)
print('See you!')