class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item #int
            self.next = next_node #IntNode

    def __init__(self):
        self.first = None #initialize an empty list

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)

    #1.1
    def insert(self, item, position):
        new_node = self.IntNode(item, None)

        if self.first is None or position <= 0:
            new_node.next = self.first
            self.first = new_node
            return
        
        current = self.first
        index = 0
        while current.next != None and index < position -1:
            current = current.next
            index += 1
            
        new_node.next = current.next
        current.next = new_node

    #1.2
    def reverse(self):
        current = self.first
        next_node = None

        while current is not None:
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp

        self.first = next_node
    
    #1.4
    def rec_reverse(self):
        def recursive_reverse(current, prev):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return recursive_reverse(next_node, current)

        self.first = recursive_reverse(self.first, None)

    def replicate(self):
        current = self.first
        while current != None:
            item = current.item
            next_node = current.next
            for _ in range(item - 1):
                new_node = self.IntNode(item, next_node)
                current.next = new_node
                current = new_node
            current = next_node
        
    
    def equals(self, anotherList):
        list1 = self.first
        list2 = anotherList.first

        while list1 is not None and list2 is not None:
            if list1.item != list2.item:
                return False
            list1 = list1.next
            list2 = list2.next
        if list1 is not None or list2 is not None:
            return False

        return True
    
    def display(self):
        current = self.first
        while current is not None:
            print(current.item, end=" -> ")
            current = current.next
        print()  # To indicate the end of the list


if __name__ == '__main__':

  #Testing 1.1
  L_insert = SLList()
  L_insert.insert(5, 0)
  L_insert.insert(6,1)
  L_insert.insert(2, 2)
  L_insert.insert(10,1)

  L_expect_insert = SLList()
  L_expect_insert.insert(5,0)
  L_expect_insert.insert(10,1)
  L_expect_insert.insert(6,2)
  L_expect_insert.insert(2,3)
  print("1.1:")
  if L_insert.equals(L_expect_insert):
      print("Two lists are equal, tests passed")
  else:
      print("Two lists are not equal, tests failed")

  L_insert = SLList()
  L_insert.insert(5,0)
  L_insert.insert(6,1)
  L_insert.insert(2,2)
  L_insert.insert(10,7)

  L_expect_insert = SLList()
  L_expect_insert.insert(5,0)
  L_expect_insert.insert(6,1)
  L_expect_insert.insert(2,2)
  L_expect_insert.insert(10,3)
  print("1.1:")
  if L_insert.equals(L_expect_insert):
      print("Two lists are equal, tests passed")
  else:
      print("Two lists are not equal, tests failed")

  #Testing 1.2
  L_reverse = SLList()
  L_reverse.addFirst(15)
  L_reverse.addFirst(10)
  L_reverse.addFirst(5)
  L_reverse.reverse()

  L_expect_reverse = SLList()
  L_expect_reverse.addFirst(5)
  L_expect_reverse.addFirst(10)
  L_expect_reverse.addFirst(15)
  print("1.2:")
  if L_reverse.equals(L_expect_reverse):
      print("Two lists are equal, tests passed")
  else:
      print("Two lists are not equal, tests failed")
  

  # Testing 1.3
  L_replicate = SLList()
  L_replicate.addFirst(3)
  L_replicate.addFirst(2)
  L_replicate.addFirst(1)
  L_replicate.replicate()
  

  L_expect_replicate = SLList()
  L_expect_replicate.addFirst(3)
  L_expect_replicate.addFirst(3)
  L_expect_replicate.addFirst(3)
  L_expect_replicate.addFirst(2)
  L_expect_replicate.addFirst(2)
  L_expect_replicate.addFirst(1)
  print("1.3:")
  if L_replicate.equals(L_expect_replicate):
      print("Two lists are equal, tests passed")
  else:
      print("Two lists are not equal, tests failed")
    
  #1.4
  L_recreverse = SLList()
  L_recreverse.addFirst(15)
  L_recreverse.addFirst(10)
  L_recreverse.addFirst(5)
  L_recreverse.rec_reverse()

  L_expect_recreverse = SLList()
  L_expect_recreverse.addFirst(5)
  L_expect_recreverse.addFirst(10)
  L_expect_recreverse.addFirst(15)
  print("1.4:")
  if L_recreverse.equals(L_expect_recreverse):
      print("Two lists are equal, tests passed")
  else:
      print("Two lists are not equal, tests failed")