from collections import deque


class Queue(object):

    def __init__(self, items=None):
        self.items = deque(items) if items else deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.popleft()

    def peek(self):
        return self.items[0]

    @property
    def empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.items)

    def __bool__(self):
        return not self.empty


class Stack(object):

    def __init__(self, items=None):
        self.items = items or []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    @property
    def empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.items)

    def __bool__(self):
        return not self.empty
