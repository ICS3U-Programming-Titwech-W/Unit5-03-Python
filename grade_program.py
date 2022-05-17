#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.12 .2022

# program gets the percentage grade when the
# user eneters their level


def calc_level(level):

    # converts from level to percenatge
    levels = {
       "1+": "Level {} has the middle percentage of 51% ".format(level),
       "1": "Level {} has the middle percentage of 55%".format(level),
       "1-": "Level {} has the middle percentage of 58%".format(level),
       "2+": "Level {} has the middle percentage of 61%".format(level),
       "2": "Level {} has the middle percentage of 65%".format(level),
       "2-": "Level {} has the middle percentage of 68%".format(level),
       "3+": "Level {} has the middle percentage of 71%".format(level),
       "3": "Level {} has the middle percentage of 75%".format(level),
       "3-": "Level {} has the middle percentage of 78%".format(level),
       "4+": "Level {} has the middle percentage of 83%".format(level),
       "4": "Level {} has the middle percentage of 91%".format(level),
       "4-": "Level {} has the middle percentage of 98%".format(level),
    }
    return levels.get(level, "Enter a vaild grade")


def main():

    # get user grade
    grade_input = input("Enter the level to convert to percentage: ")

    # call the function
    percentage = calc_level(grade_input)

    if calc_level(grade_input) == "-1":
        print("Invalid entry.")
    else:
        print(percentage)


if __name__ == "__main__":
    main()
