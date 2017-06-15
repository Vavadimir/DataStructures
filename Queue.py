class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def shift(self, obj):
        if self.tail is None and self.head is None:
            self.head = QueueNode(obj, None, None)
            self.tail = self.head
        elif self.head == self.tail and self.tail.value != obj:
            self.tail = QueueNode(obj, None, self.head)
            self.head.next = self.tail
        else:
            self.tail.next = QueueNode(obj, None, self.tail)
            self.tail = self.tail.next

    def unshift(self):
        if self.head is None:
            return None
        elif self.tail is None :
            return self.head.value
        else:
            temp = self.head
            self.head = self.head.next
            return temp.value

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def count(self):
        counter = 0
        temp = self.head
        while True:
            if temp is None:
                return counter
            else:
                counter += 1
                temp = temp.next
