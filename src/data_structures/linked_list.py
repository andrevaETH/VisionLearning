# -*- coding: utf-8 -*-
"""
Created on Dec 7 2017 1:53 PM
@author: andrevaETH
"""

class Node:
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

    def update_previous_node(self, previous_node):
        """
        Change the pointer to previous_node
        """
        self.previous = previous_node

    def update_next_node(self, next_node):
        """
        Change the pointer to next_node
        """
        self.next = next_node

class LinkedList:
    """
    Class for testing a LinkedList
    """
    def __init__(self, first_value):
        """
        Constructor
        """
        # - Otherwise add a node -
        new_node = Node(first_value)
        self.first_node = new_node
        self.last_node = new_node

    def add_node_last(self, node_value):
        """
        Add a node at the end of the LinkedList
        """
        new_node = Node(node_value, None, self.last_node)

        # - Set last_node accordingly -
        self.last_node = new_node

    def add_node_first(self, node_value):
        """
        Add a node at the head
        """
        new_node = Node(node_value, self.first_node, None)

        # - Update head -
        self.first_node = new_node
