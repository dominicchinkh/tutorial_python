#!/bin/python3

# A linked list has a cycle if traversing it visits any node more than once.
# Given a pointer to the list head, return 1 if a cycle exists or 0 otherwise.
#
# Example
# head -> 1 -> 2 -> 3 -> NULL has no cycle (node numbers shown), so return 0.
# head -> 1 -> 2 -> 3 -> 1 -> NULL has node 3 linking back to node 1, so return 1.
#
# Function Description
# Implement has_cycle with parameter:
# - SinglyLinkedListNode pointer head: reference to the list head
#
# Returns
# - int: 1 when a cycle is present, 0 when absent
# Note: An empty list has a null head.
#
# Input Format
# Input is read from stdin and passed to the function; custom test case details are omitted due to complexity.
#
# Constraints
# - 0 <= list size <= 1000
#
# Sample Input
# Two linked list references are passed: one single-node list pointing to null, and one three-node list where node 3 loops back to node 2.
#
# Sample Output
# 0
# 1

# OUTPUT_PATH=/dev/stdout python3 -m linked_list.singly.has_cycle

import os

from data_structure.singly_linked_list import SinglyLinkedList, SinglyLinkedListNode

def has_cycle(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow is fast:
            return 1
        
    return 0

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as file:
        test_case_count = int(input().strip())
        
        for _ in range(test_case_count):
            index = int(input().strip())
            count = int(input().strip())
            
            l = SinglyLinkedList()
            for _ in range(count):
                l.insert_node(int(input().strip()))
        
            extra = SinglyLinkedListNode(-1);
            temp = l.head;

            for i in range(count):
                if i == index:
                    extra = temp

                if i != count-1:
                    temp = temp.next

            temp.next = extra

            result = has_cycle(l.head)
        
            file.write(str(int(result)) + '\n')
