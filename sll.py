class SLL:
	class _Node:
		def __init__(self, item, next):
			self._item = item
			self._next = next

	def __init__(self):
		self.clear()

	def __len__(self):
		n = 0
		r = self._head;
		while r is not None:
			n += 1
			r = r._next
		return n

	def isEmpty(self):
		return self._head is None

	def pop(self):
		item = self._head._item
		self._head = self._head._next
		if self.isEmpty():
			self._tail = None
		return item

	def clear(self):
		self._head = None
		self._tail = None

	def push(self, item):
		node = self._Node(item, self._head)
		if self.isEmpty():
			self._tail = node
		self._head = node

	def append(self, item):
		if self.isEmpty():
			self.push(item)
		node = self._Node(item, None)
		self._tail._next = node
		self._tail = node


sll = SLL()
for i in range(5):
	sll.push(i)
	sll.append(i)

while not sll.isEmpty():
	print(sll.pop())
