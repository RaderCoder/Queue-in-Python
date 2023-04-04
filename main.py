import Queue

if __name__ == "__main__":
    Q = Queue.Queue()
    print(Q.is_null())
    # print(Q)

    Q.enqueue(3)

    Q.enqueue(4)

    Q.dequeue()

    # print(Q)

    # print(Q.peek())

    # print(Q.is_null())

    

