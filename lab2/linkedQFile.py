class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedQ:
    def __init__(self, first = None, last= None):
        self.__first = first
        self.__last = last

    def enqueue(self, value):
        if(self.isEmpty()):
            self.__first = Node(value)
        else:
            if(self.__last == None):
                self.__last = Node(value)
                self.__first.next = self.__last
            else:
                self.__last.next = Node(value)
                self.__last = self.__last.next
        return

    def dequeue(self):
        if(not self.isEmpty()):
            temp_value = self.__first.value
            self.__first = self.__first.next
            return temp_value
        else:
            return

    def isEmpty(self):
        if(self.__first == None):
            return True
        else:
            return False

    def size(self):
        counter = 0
        temp_node = self.__first
        while temp_node.next != None:
            temp_node = temp_node.next
            counter += 1
        return counter

if __name__ == "__main__":
    import unittest
    from linkedQFile import LinkedQ

    class TestQueue(unittest.TestCase):

        def test_isEmpty(self):
            #isEmpty ska returnera True för tom kö, False annars
            q = LinkedQ()
            self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
            q.enqueue(17)
            self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

        def test_order(self):
            #Kontrollerar att kö-ordningen blir rätt
            q = LinkedQ()
            q.enqueue(1)
            q.enqueue(2)
            q.enqueue(3)
            self.assertEqual(q.dequeue(), 1)
            self.assertEqual(q.dequeue(), 2)
            self.assertEqual(q.dequeue(), 3)

    if __name__ == "__main__":
        unittest.main()
