class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.peek())    # 10
print(q.dequeue()) # 10
print(q.dequeue()) # 20
print(q.dequeue()) # 30
print(q.dequeue()) # Queue is empty
