class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if self.current + 1  == self.capacity:
      self.current = 0
    else:
      self.current += 1
  def get(self):
    not_none = [i for i in self.storage if i is not None]
    return not_none




buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.get())