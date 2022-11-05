#Author: Faith Elledge
#Githubuser: elledgef
#Date: 11/4/22
#Description: This code takes a list of numbers and returns True if they are decreasing and False if the list does
#anything otherwise

def is_decreasing(num_list):
    """ This function takes a list of numbers for its parameter then outputs true if the values on the list are
    decreasing and False if they sre increasing or any other pattern"""
    if len(num_list) == 2:
        return True
    elif num_list[0] > num_list[1]:
        return True
    else:
        if num_list [0] < num_list[1]:
            return False
        else:
            return is_decreasing(num_list[1:])















