class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        if self.begin is None and self.end is None:
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin
        elif self.end == self.begin:
            self.end = DoubleLinkedListNode(obj, None, self.begin)
            self.begin.next = self.end
        else:
            self.end.next = DoubleLinkedListNode(obj, None, self.end)
            self.end = self.end.next

    def pop(self):
        if self.begin is None:
            return None
        if self.end is None:
            temp = self.begin
            self.begin = None
            return temp.value
        if self.begin == self.end:
            temp = self.begin
            self.begin = None
            self.end = None
            return temp.value
        else:
            temp = self.end
            self.end = self.end.prev
            self.end.next = None
            return temp.value

    def shift(self, obj):
        if self.begin is None and self.end is None:
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin
        elif self.end == self.begin:
            self.begin = DoubleLinkedListNode(obj, self.end, None)
            self.end.prev = self.begin
        else:
            temp = self.begin
            self.begin = DoubleLinkedListNode(obj, temp, None)

    def unshift(self):
        temp = self.begin
        if temp is None:
            return None
        self.begin = self.begin.next
        if self.begin is not None:
            self.begin.prev = None
        return temp.value

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove().  It should take a node, and detach it from
        the list, whether the node is at the front, end, or in the middle."""
        temp = self.begin
        while True:
            if (temp.value == node.value) and (temp.next.value == node.next) and (temp.prev.value == node.prev):
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                break
            else:
                temp = temp.next
                if temp is None:
                    break

    def remove(self, obj):
        temp = self.begin
        counter = 0
        if temp.value == obj:
            self.begin = temp.next
            if self.begin is not None:
                self.begin.prev = None
            return counter
        else:
            while True:
                counter += 1
                if temp.next.value == obj:
                    temp.next = temp.next.next
                    if temp.next is not None:
                        temp.next.prev = temp
                    return counter
                else:
                    temp = temp.next

    def first(self):
        return self.begin.value

    def last(self):
        return self.end.value

    def count(self):
        counter = 0
        temp = self.begin
        while True:
            if temp is None:
                return counter
            counter += 1
            temp = temp.next


    def get(self, index):
        counter = 0
        temp = self.begin
        if self.count() <= index:
            return None
        else:
            while True:
                if counter == index:
                    return temp.value
                counter += 1
                temp = temp.next

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""