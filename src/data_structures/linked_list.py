# -*- coding: utf-8 -*-
"""
Created on Dec 7 2017 1:53 PM
@author: andrevaETH
"""

class Node(object):
    """
    Implementation of the Node Class
    """
    def __init__(self, data_value=None, next_node=None, previous_node=None):
        """
        Constructor
        """
        self.data = data_value
        self.next = next_node
        self.previous = previous_node

    def update_node(self, next_node, previous_node):
        """
        Change the node pointers
        """
        self.next = next_node
        self.previous = previous_node


class LinkedList(object):
    """
    Class for testing a LinkedList
    """
    def __init__(self, first_value=None):
        """
        Constructor
        """
        # - If first_value is not None add a node -
        if(first_value != None):
            new_node = Node(first_value)
            self.first_node = new_node
            self.last_node = new_node
        else:
            self.first_node = None
            self.last_node = None

    def create_first_node(self, head_value):
        """
        Creates the head if not yet done
        """
        new_node = Node(first_value)
        self.first_node = new_node
        self.last_node = new_node

    def add_node_last(self, node_value):
        """
        Add a node at the end of the LinkedList
        """
        new_node = Node(node_value, None, self.last_node)

        # - Update the Nodes -
        self.last_node.update_node(new_node, self.last_node.previous)
        self.last_node = new_node

    def add_node_first(self, node_value):
        """
        Add a node at the head
        """
        new_node = Node(node_value, self.first_node, None)

        # - Update head -
        self.first_node.update_node(self.first_node.next, new_node)
        self.first_node = new_node

    def find(self, data_value):
        """
        Method to find a value in the LinkedList and return boolean
        """
        current_node = self.first_node
        while(current_node.data != data_value):
            current_node = current_node.next

            # - If end of LinkedList is reached abort -
            if(current_node == None):
                return False

        return True

    def clear(self):
        """
        Remove all Nodes from the list
        """
        current_node = self.first_node
        while(current_node.next != None):
            del current_node
