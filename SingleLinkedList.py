class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        if self.begin is None and self.end is None:
            self.end = SingleLinkedListNode(obj, None)
            self.begin = self.end
        elif self.begin == self.end: #and self.begin.value == self.end.value and self.end.value != obj:
            self.end = SingleLinkedListNode(obj, None)
            self.begin.next = self.end
        else:
            self.end.next = SingleLinkedListNode(obj, None)
            self.end = self.end.next


    def pop(self):
        if self.begin is None:
            return None
        if self.end is None:
            temp = self.begin
            self.begin = None
            return temp.value
        else:
            temp = self.begin
            cnt = 0
            while True:
                if temp.next == self.end:
                    if cnt == 0:
                        temp = self.end
                        self.begin.next = None
                        self.end = None
                        return temp.value
                    end = self.end
                    self.end = temp
                    self.end.next = None
                    return end.value
                else:
                    temp = temp.next
                    cnt += 1

    def shift(self, obj):
        if self.begin is None and self.end is None:
            self.end = SingleLinkedListNode(obj, None)
            self.begin = self.end
        elif self.begin == self.end:
            self.begin = SingleLinkedListNode(obj, self.end)
        else:
            temp = self.begin
            self.begin = SingleLinkedListNode(obj, temp)

    def unshift(self):
        if self.begin is None:
            return None
        temp = self.begin
        self.begin = temp.next
        return temp.value

    def remove(self, obj):
        temp = self.begin
        counter = 0
        if temp.value == obj:
            self.begin = temp.next
            return counter
        else:
            while True:
                counter += 1
                if temp.next.value == obj:
                    temp.next = temp.next.next
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

    def dump(self):
        self.begin = None
        self.end = None
