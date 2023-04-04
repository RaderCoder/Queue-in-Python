### Queue in Python

Decided to implement queue in python. This is a linked list implementation.

#### What is a Queue?

A Queue is a data structure that follows the first in first out principle. Think of a line in front of the cashier at a supermarket. The first person in the line is the first to get served. Once they are served, they then leave the line. Hence, the first item in the queue is also the first to leave.

A linked list is an intuitive data structure to implement a queue. You can see that the linked list is basically a queue itself, depending on how you choose to implement it. The queue has a front value. This value will refer to the first item of the list. As in, the first item inserted.

#### Queue Functions

- Enqueue: Insert an item into the queue. The item will be inserted at the back of the queue. We will have the head point to this item and use it to refer to the back of the queue. We can use the push method from the linked list.
- Dequeue: Remove an item from the queue. We could use the delete node function, however we will have to assign a new front value. This may result in iterating over the queue twice. Thus, we write our own function for the queue.
- Peek: Returns the value of the front item.
- Rear: Returns the value of the last item.
- Is_null: Checks to see if the queue is empty. All we have to do is check the head node. If it has no value assigned, the queue is empty.