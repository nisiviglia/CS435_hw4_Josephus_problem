##
# @file cll.py
# @brief A circular doubly linked list implementation
# @author Nicholas Siviglia (31360256)
# @version 1
# @date 2018-03-05

class CLL:

    class _Node:
        def __init__(self, item, next, prev):
            self._item = item
            self._next = next
            self._prev = prev

    def __init__(self):
        self.clear()

    def clear(self):
        self._head = None

    def len(self):
        if self._head == None:
            return 0
        n = 1
        r = self._head;
        head_id = id(self._head)
        while id(r._next) != head_id:
            n += 1
            r = r._next
        return n

    def isEmpty(self):
            return self._head is None

    def push(self, item):
        node = self._Node(item, None, None)
        if self.isEmpty():
            self._head = node
            self._head._next = node
            self._head._prev = node
        else:
            r = self._head
            head_id = id(self._head)
            while(id(r._next) != head_id):
                r = r._next
            r._next = node
            self._head._prev = node
            node._prev = r
            node._next = self._head

    def peek(self):
        return self._head._item

    def pop(self, direction):
        if direction == 'c':
           return self.pop_clockwise()
        elif direction == 'u':
            return self.pop_anticlockwise()
        else:
            print("Invalid direction")


    def pop_clockwise(self):
        r = self._head
        head_id = id(self._head)
        while(id(r._next) != head_id):
            r = r._next
        if(id(r) == head_id):
            self.clear()
            return r._item
        else:
            rtn = self._head
            self._head = self._head._next
            self._head._prev = r
            r._next = self._head
            return rtn._item

    def pop_anticlockwise(self):
        r = self._head
        head_id = id(self._head)
        while(id(r._prev) != head_id):
            r = r._prev
        if(id(r) == head_id):
            self.clear()
            return r._item
        else:
            rtn = self._head
            self._head = self._head._prev
            self._head._next = r
            r._prev = self._head
            return rtn._item

    def shift(self, direction):
        if direction == 'c':
            self.shift_clockwise()
        elif direction == 'u':
            self.shift_anticlockwise()
        else:
            print("Invalid direction")

    def shift_clockwise(self):
        self._head = self._head._next

    def shift_anticlockwise(self):
        self._head = self._head._prev


