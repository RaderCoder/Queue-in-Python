import Queue

if __name__ == "__main__":
    Q = Queue.Queue(5)

    # print(Q)

    Q.enqueue(3)

    Q.enqueue(4)

    Q.dequeue()

    # print(Q.front.value)