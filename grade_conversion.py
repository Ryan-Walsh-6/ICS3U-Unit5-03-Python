#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program converts the level to grae and returns a middle percentage mark

def grade_conversion(grade_from_user):
    # calculates area

    # process & output
    if grade_from_user == "4+":
        percentage = 97
    elif grade_from_user == "4":
        percentage = 90
    elif grade_from_user == "4-":
        percentage = 83
    elif grade_from_user == "3+":
        percentage = 78
    elif grade_from_user == "3":
        percentage = 75
    elif grade_from_user == "3-":
        percentage = 71
    elif grade_from_user == "2+":
        percentage = 68
    elif grade_from_user == "2":
        percentage = 65
    elif grade_from_user == "2-":
        percentage = 61
    elif grade_from_user == "1+":
        percentage = 58
    elif grade_from_user == "1":
        percentage = 55
    elif grade_from_user == "1-":
        percentage = 51
    elif grade_from_user == "R":
        percentage = 30
    else:
        percentage = -1

    return percentage


def main():
    # this program calculates the area of a triangle
    # input
    grade_from_user = input("Enter the level you want converted to a"
                            " percentage:")
    print("\n", end="")

    # call function
    converted_grade = grade_conversion(grade_from_user)

    if converted_grade == -1:
        print("Level {0} is not a valid entry.".format(grade_from_user))
    else:
        print("Level {0} has a middle percentage of {1}%."
              .format(grade_from_user, converted_grade))


if __name__ == "__main__":
    main()
