# -*- coding: utf-8 -*-
"""
Created on Dec 20 2017 1:53 PM
@author: andrevaETH
"""
import src.data_structures.LL.linked_list

class NumberLinkedList(src.data_structures.linked_list.LinkedList):
    """
    Class which uses the LinkedList implementation to store big numbers
    """

    def __init__(self, number_as_string, base=10):
        """
        Constructor for a very long number. The default base is 10.
        """
        # - Call the Super Constructor -
        super(NumberLinkedList, self).__init__()

        # - Save the number as the linked_list -
        self.save_number(number_as_string)
        self.base = base

    def reverse_string(self, number_as_string):
        """
        Reverses the order of the string e.g. "123" >> "321"
        """
        return number_as_string[::-1]

    def save_number(self, number_as_string):
        """
        Takes string and saves in a LinkedList
        """
        # - Get the length of the string and reverse the string -
        str_len = len(number_as_string)
        rev_number = self.reverse_string(number_as_string)
        power_of_base = 0

        # - Iterate through the reversed number -
        for el in rev_number:
            # - Convert string to int -
            curr_el = int(el)

            # - Store the power and current number in a dictionary and add node -
            n_dict = {'power': power_of_base, 'value': curr_el}
            if(power_of_base == 0):
                self.create_first_node(n_dict)
            else:
                self.add_node_last(n_dict)

            power_of_base += 1

    def print_number(self):
        """
        Method to print number as string back to display
        """
        current_node = self.first_node
        result_number = ""
        while(current_node != None):

            result_number += str(current_node.data['value'])

            current_node = current_node.next
        print(self.reverse_string(result_number))
