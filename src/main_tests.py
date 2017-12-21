# -*- coding: utf-8 -*-
"""
Created on Dec 6 2017 1:53 PM
@author: andrevaETH
"""

import data_structures.LL.linked_list as ll
import data_structures.LL.ll_numbers as nll

def base_operations():
    """
    Many test operations in python
    """
    maxLen = -1
    if(maxLen > 5):
        print("Hello world " + str(maxLen))
    elif(maxLen < 0):
        print("bla")
    else:
        return 0

    i = 0
    while(i < 5):
        print("Sod it")
        i += 1

    # - Create a switch statement replacement -
    switchDict = {'a' : 1, 'b' : 2}

    keyForDict = 'a'
    print(switchDict.get(keyForDict, 'default'))

    yourAge = input("Please enter your age: ")
    print("You are " + yourAge + " years old.")

def main():
    link_list = ll.LinkedList(3)

    # - Make a linked list for a very large number -
    # - Rather pointless in python as seen by the comparison -
    a = "73928792834792837497842978080123801931083098"
    n_link_list = nll.NumberLinkedList(a)
    n_link_list.print_number()

    b = int(73928792834792837497842978080123801931083098)
    print("Ordinary way to store number ", str(b))

    # - Add a value -
    link_list.add_node_last(5)

    # - Print value -
    print(str(link_list.last_node.data))

if __name__ == '__main__':
    main()
