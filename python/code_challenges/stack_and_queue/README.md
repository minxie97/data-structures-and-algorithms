# Stacks and Queues

## Challenge
* The challenge was to implement both a stack and a queue using linked lists as an underlying data storage mechanism

## Approach & Efficiency
* The approach was to utilize the knowledge gained from the reading and lecture to implement the features. Wrote tests first and created methods that fulfilled requirements. Acheived 100% coverage.

## API
* N/A

# Pseudo Queue
* Implement a first in first out "queue" using two stacks

## Whiteboard Process
![Challenge 11 Whiteboard](https://github.com/minxie97/data-structures-and-algorithms/blob/stack-queue-pseudo/python/code_challenges/stack_and_queue/stack-queue-pseudo.jpg)

## Approach & Efficiency
* The approach was to use one stack as the main stack and the other as a holder stack. anytime something gets added, everything from the first stack and moved to the second stack before the new value is added. Once added, everything from the second stack is moved back to the first. To dequeue, we just need to pop from the first stack.
* For enqueue the complexity is O(N) as efficiency decreases depending on size of current pseudo queue
* For dequeue the complexity of O(1) as it is a simple pop

## Solution
* [Code](https://github.com/minxie97/data-structures-and-algorithms/blob/stack-queue-pseudo/python/code_challenges/stack_and_queue/pseudoqueue.py)
* [Tests](https://github.com/minxie97/data-structures-and-algorithms/blob/stack-queue-pseudo/python/code_challenges/stack_and_queue/test_stack_and_queue.py)


