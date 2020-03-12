class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    #prev is set to None before Head
    previous = None
    #current is set to the first value in the list, or the head
    current = self.head 
    #loop will move current and previous down the list to the end, when it reached the last element in the LL it's next value will be None and the loop will break
    while(current is not None): 
        #reference the node's *next_value
        next = current.next_node
        #assign the current node's next as previous node, if at start of loop, the heads next will now be None
        current.next_node = previous 
        #move previous up the list by assigning it to current Node
        previous = current
        #move surrent up the list by assigning it to the current node's *next_value 
        current = next
    #when loop is finished, assign the head as previous(which is at the end of the list now) to finish reversing the list
    self.head = previous



list = LinkedList()

list.add_to_head(1)
print(list.reverse_list())