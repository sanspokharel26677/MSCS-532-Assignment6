"""
This Python script contains implementations of basic data structures:
1. Arrays and Matrices
2. Stacks and Queues (using arrays)
3. Singly Linked List
It also allows interaction with these structures via a simple text-based interface.
You can add, delete, and perform other operations interactively.
Each data structure starts with some dummy data to test and play around with.
"""

# Array implementation
class MyArray:
    """ 
    This class implements basic array operations like insert, delete, and access.
    The array starts with some dummy data to showcase its use.
    """
    def __init__(self):
        self.array = [1, 2, 3, 4, 5]  # Initial dummy data to get started

    def insert(self, value):
        """ 
        Adds an element to the end of the array. 
        """
        self.array.append(value)  # Insert at the end of the array

    def delete(self, index):
        """ 
        Deletes an element at a specific index. 
        Will print error message if the index is out of bounds.
        """
        if 0 <= index < len(self.array):
            self.array.pop(index)  # Remove element at the given index
        else:
            print(f"Index {index} is out of bounds. Can't delete here!")

    def access(self, index):
        """ 
        Returns the element at the specified index. 
        Handles out of bounds situations.
        """
        if 0 <= index < len(self.array):
            return self.array[index]  # Return the element at the index
        else:
            return f"Index {index} is out of bounds."

    def display(self):
        """ 
        Displays the array elements.
        """
        print(f"Current array: {self.array}")  # Print the array to the console
        
# Matrix implementation
class MyMatrix:
    """ 
    This class implements basic matrix operations like insert, delete, and access.
    The matrix starts with some dummy data for demonstration.
    """
    def __init__(self):
        # Initialize a 3x3 matrix with dummy data
        self.matrix = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]

    def insert(self, row, col, value):
        """ 
        Inserts a value at the specified row and column.
        Assumes the row and column are within bounds.
        """
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            self.matrix[row][col] = value  # Replace value at the given position
        else:
            print("Row or column out of bounds!")

    def delete(self, row, col):
        """ 
        Deletes a value at the specified row and column by setting it to zero.
        Assumes the row and column are within bounds.
        """
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            self.matrix[row][col] = 0  # Set the value to zero (could simulate deletion)
        else:
            print("Row or column out of bounds!")

    def access(self, row, col):
        """ 
        Returns the value at the specified row and column.
        """
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            return self.matrix[row][col]  # Return the value
        else:
            return "Row or column out of bounds!"

    def display(self):
        """ 
        Displays the matrix in a formatted way.
        """
        for row in self.matrix:  # Iterate over each row
            print(row)  # Print each row


# Stack implementation using an array
class Stack:
    """ 
    Stack class where we can push elements to the top and pop from the top. 
    It starts with some dummy values.
    """
    def __init__(self):
        self.stack = [10, 20, 30]  # Dummy values to start with

    def push(self, value):
        """ Adds an element to the top of the stack. """
        self.stack.append(value)  # Add the value to the top of the stack

    def pop(self):
        """ Removes and returns the top element of the stack. """
        if not self.is_empty():
            return self.stack.pop()  # Remove the last item from the stack
        else:
            return "Stack is empty!"  # If stack is empty, return this message

    def is_empty(self):
        """ Checks if the stack is empty. """
        return len(self.stack) == 0  # If no elements, it's empty

    def display(self):
        """ 
        Displays the current stack elements. 
        """
        print(f"Current stack: {self.stack}")  # Print the stack contents

# Queue implementation using an array
class Queue:
    """ 
    Queue class with basic enqueue and dequeue operations. 
    It starts with some dummy values.
    """
    def __init__(self):
        self.queue = [100, 200, 300]  # Dummy values to play with

    def enqueue(self, value):
        """ Adds an element to the end of the queue. """
        self.queue.append(value)  # Add value to the end of the queue

    def dequeue(self):
        """ Removes and returns the front element of the queue. """
        if not self.is_empty():
            return self.queue.pop(0)  # Remove the first element
        else:
            return "Queue is empty!"  # If queue is empty, return message

    def is_empty(self):
        """ Checks if the queue is empty. """
        return len(self.queue) == 0  # Queue is empty if length is zero

    def display(self):
        """ 
        Displays the current queue elements. 
        """
        print(f"Current queue: {self.queue}")  # Print the queue contents

# Singly linked list implementation
class Node:
    """ 
    Node class is used to represent each node in the linked list. 
    It holds data and points to the next node in the list.
    """
    def __init__(self, data=None):
        self.data = data  # Store the data value
        self.next = None  # Pointer to the next node (initially None)

class LinkedList:
    """ 
    Linked list implementation. 
    Starts with a few dummy nodes to demonstrate insertion and traversal.
    """
    def __init__(self):
        self.head = None  # Start with an empty list
        self.insert(11)  # Insert dummy data 11
        self.insert(22)  # Insert dummy data 22
        self.insert(33)  # Insert dummy data 33

    def insert(self, data):
        """ Inserts a new node at the end of the linked list. """
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If list is empty, set new node as head
        else:
            current = self.head  # Start from the head
            while current.next:  # Traverse to the end
                current = current.next
            current.next = new_node  # Attach new node to the end

    def delete(self, data):
        """ Deletes the first node that contains the given data. """
        if self.head is None:
            print("List is empty!")  # If no nodes, can't delete anything
            return
        if self.head.data == data:
            self.head = self.head.next  # If head has the data, remove the head
        else:
            current = self.head  # Start from the head
            while current.next and current.next.data != data:
                current = current.next  # Move to the next node
            if current.next is None:
                print(f"Element {data} not found!")  # Element doesn't exist
            else:
                current.next = current.next.next  # Bypass the node to delete

    def traverse(self):
        """ 
        Traverses the list and prints all the nodes' data. 
        """
        current = self.head  # Start from the head
        if current is None:
            print("The list is empty.")  # If no nodes, it's empty
            return

        while current:
            print(current.data, end=" -> ")  # Print each node's data
            current = current.next  # Move to the next node
        print("None")  # End of the list



def main():
    """ 
    This function runs an interactive program allowing users to play with arrays, stacks, queues, linked lists, and matrices.
    It lets you insert, delete, or display the contents of each data structure.
    Now, after each operation, the user is notified that the action has been successfully completed.
    """
    my_array = MyArray()  # Create an array instance
    my_stack = Stack()  # Create a stack instance
    my_queue = Queue()  # Create a queue instance
    my_linked_list = LinkedList()  # Create a linked list instance
    my_matrix = MyMatrix()  # Create a matrix instance

    while True:
        # Display choices for interacting with the data structures
        print("\nChoose a data structure to interact with:")
        print("1. Array")
        print("2. Stack")
        print("3. Queue")
        print("4. Linked List")
        print("5. Matrix")
        print("6. Quit")
        choice = input("Enter your choice: ")  # Get user's choice

        if choice == '1':  # If user chooses Array
            print("\nArray Operations: ")
            my_array.display()  # Show the current array
            action = input("Enter 'i' to insert, 'd' to delete, 'a' to access an element: ")  # Ask for action
            if action == 'i':
                value = int(input("Enter value to insert: "))  # Get value to insert
                my_array.insert(value)  # Insert the value
                print(f"{value} has been inserted into the array.")  # Notify user
            elif action == 'd':
                index = int(input("Enter index to delete: "))  # Get index to delete
                my_array.delete(index)  # Delete the element at the index
                print(f"Element at index {index} has been deleted.")  # Notify user
            elif action == 'a':
                index = int(input("Enter index to access: "))  # Get index to access
                print(f"Element at index {index}: {my_array.access(index)}")  # Print accessed value
            my_array.display()  # Display updated array

        elif choice == '2':  # If user chooses Stack
            print("\nStack Operations: ")
            my_stack.display()  # Show current stack
            action = input("Enter 'p' to push, 'o' to pop: ")  # Ask for action
            if action == 'p':
                value = int(input("Enter value to push: "))  # Get value to push
                my_stack.push(value)  # Push the value onto the stack
                print(f"{value} has been pushed onto the stack.")  # Notify user
            elif action == 'o':
                popped_value = my_stack.pop()  # Pop the value
                print(f"Popped value: {popped_value}")  # Notify user of the popped value
            my_stack.display()  # Display updated stack

        elif choice == '3':  # If user chooses Queue
            print("\nQueue Operations: ")
            my_queue.display()  # Show current queue
            action = input("Enter 'e' to enqueue, 'd' to dequeue: ")  # Ask for action
            if action == 'e':
                value = int(input("Enter value to enqueue: "))  # Get value to enqueue
                my_queue.enqueue(value)  # Enqueue the value
                print(f"{value} has been enqueued into the queue.")  # Notify user
            elif action == 'd':
                dequeued_value = my_queue.dequeue()  # Dequeue the value
                print(f"Dequeued value: {dequeued_value}")  # Notify user of the dequeued value
            my_queue.display()  # Display updated queue

        elif choice == '4':  # If user chooses Linked List
            print("\nLinked List Operations: ")
            my_linked_list.traverse()  # Show current linked list
            action = input("Enter 'i' to insert, 'd' to delete: ")  # Ask for action
            if action == 'i':
                value = int(input("Enter value to insert: "))  # Get value to insert
                my_linked_list.insert(value)  # Insert the value into the list
                print(f"{value} has been inserted into the linked list.")  # Notify user
            elif action == 'd':
                value = int(input("Enter value to delete: "))  # Get value to delete
                my_linked_list.delete(value)  # Delete the value from the list
                print(f"Value {value} has been deleted from the linked list.")  # Notify user
            my_linked_list.traverse()  # Display updated linked list

        elif choice == '5':  # If user chooses Matrix
            print("\nMatrix Operations: ")
            my_matrix.display()  # Show the current matrix
            action = input("Enter 'i' to insert, 'd' to delete, 'a' to access an element: ")  # Ask for action
            if action == 'i':
                row = int(input("Enter row index to insert: "))  # Get row index
                col = int(input("Enter column index to insert: "))  # Get column index
                value = int(input("Enter value to insert: "))  # Get value to insert
                my_matrix.insert(row, col, value)  # Insert the value into the matrix
                print(f"{value} has been inserted into the matrix at position ({row}, {col}).")  # Notify user
            elif action == 'd':
                row = int(input("Enter row index to delete: "))  # Get row index
                col = int(input("Enter column index to delete: "))  # Get column index
                my_matrix.delete(row, col)  # Delete the value from the matrix
                print(f"Value at position ({row}, {col}) has been deleted from the matrix.")  # Notify user
            elif action == 'a':
                row = int(input("Enter row index to access: "))  # Get row index
                col = int(input("Enter column index to access: "))  # Get column index
                print(f"Element at ({row}, {col}): {my_matrix.access(row, col)}")  # Print accessed value
            my_matrix.display()  # Display updated matrix

        elif choice == '6':  # If user chooses to quit
            print("Exiting the program. Goodbye!")  # Exit message
            break  # Break out of the loop

        else:
            print("Invalid choice. Please try again.")  # Handle invalid input



# Running the interactive program
if __name__ == "__main__":
    main()  # Call main function to start the program

