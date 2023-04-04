import LinkedList

class Queue(LinkedList.LinkedList):
    def __init__(self, head=None):
        super().__init__(head)
        self.front = self.head

    def enqueue(self, data):
        self.push(data)

    def dequeue(self):
        temp = self.head
        while temp.next != self.front:
            temp = temp.next

        val = self.front.value
        self.front = temp
        self.front.next = None

        return val

    def peek(self):
        return self.front.value
    
    def rear(self):
        return self.head.value
    
    def is_null(self):
        return False if self.head.value else True