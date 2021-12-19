# Singly Linked List
* A linked list is a sequence of data elements. Each element, called a node, contains whatever value and a pointer that points to the next node in the sequence. 

## Challenge
* Implement a linked list. 
    * Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    * Create a Linked List class
        * Within your Linked List class, include a head property.
        * Upon instantiation, an empty Linked List should be created.

## Approach & Efficiency
* First and foremost, I had to wrap my head around the concept of a linked list. Going off of Roger's immensely helpful demo in class, I created various linked lists and used the inserts to see how the structure of the list actually worked. Once I understood how the pointers worked, it was fairly simple to traverse the list to find values.

## API
* 1. insert method that adds a new node with that value to the head of the list with an O(1) Time performance.
* 2. includes method that indicates whether that value exists as a Node’s value somewhere within the list.
* 3. to_string method that returns a string representing all the values in the Linked List
