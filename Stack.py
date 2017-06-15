class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class Stack(object):

    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = StackNode(obj, None)
        else:
            self.top = StackNode(obj, self.top)

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.value

    def top(self):
        return self.top.value

    def count(self):
        counter = 0
        temp = self.top
        while True:
            if temp is None:
                return counter
            counter += 1
            temp = temp.next

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""