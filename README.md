"""
README.py - Documentation and Execution for Stack Implementation Using Linked Lists
Author: Nagihan
Description: This Python script serves as both documentation (README) and 
a functional file that explains and tests the Stack implementation using Linked Lists.
"""

# Importing the Stack class from the ds module
from ds import Stack

# Display project details as documentation
def project_overview():
    print("""
    ============================
    Stack Implementation Using Linked Lists
    ============================

    Project Overview:
    This project demonstrates the implementation of a stack (LIFO - Last In First Out)
    data structure using linked lists. The tasks include:
    - Creating a stack class using linked list data structure.
    - Implementing stack operations: push(), pop(), and peek().
    - Testing the stack implementation via this script.
    """)

# Display class descriptions
def class_descriptions():
    print("""
    Class Definitions:
    1. LinkedListNode:
       - Represents a node in the linked list.
       - Inherits from the Node class.

    2. LinkedList:
       - Provides linked list functionalities.
       - add_node(node, index): Adds a node at the specified index.
       - remove_node(index): Removes a node from the specified index.

    3. Stack:
       - Implements the stack operations using a linked list.
       - push(data): Adds a node to the top of the stack.
       - pop(): Removes the top node from the stack.
       - peek(): Returns the top node without removing it.
    """)

# Display setup and usage instructions
def setup_and_usage():
    print("""
    Setup and Execution:
    1. Clone the repository:
       git clone <repository-link>

    2. Navigate to the repository folder:
       cd <repository-folder>

    3. Ensure Python 3.x is installed and run this script to test:
       python README.py
    """)

# Test the Stack Implementation
def test_stack():
    print("\nTesting the Stack Implementation:\n")
    
    # Creating a stack
    stack = Stack()
    print("Created a new stack.")

    # Push operations
    print("Pushing 10 onto the stack.")
    stack.push(10)
    print("Pushing 20 onto the stack.")
    stack.push(20)
    print("Pushing 30 onto the stack.")
    stack.push(30)

    # Peek operation
    print(f"Top element (peek): {stack.peek()}")

    # Pop operations
    print(f"Popped element: {stack.pop()}")
    print(f"Popped element: {stack.pop()}")
    print(f"Top element (peek): {stack.peek()}")
    
    # Final pop
    print(f"Popped element: {stack.pop()}")
    
    # Try popping from an empty stack
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error: {e}")

# Main function to execute the script
if __name__ == "__main__":
    print("Welcome to README.py for Stack Implementation\n")
    project_overview()
    class_descriptions()
    setup_and_usage()
    test_stack()