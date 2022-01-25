from array import array
class Queue:
    def __init__(self, array = []):
        self.__queue = array

    def __str__():
        temp_str
        for i in range(self.__queue):
            temp_str = temp_str + " " + self.queue[i]
        return temp_str
    def getQ():
        return self.__queue

    def setQ(index, value):
        self.__queue[index] = value
        return

    def enqueue(self, value):
        self.__queue.append(value)
        return

    def dequeue(self):
        if (not self.isEmpty()):
            temp_value = self.__queue.pop(0)
            return temp_value
        else:
            print("The queue is empty")
            return

    def isEmpty(self):
        if(self.size()==0):
            return True
        else:
            return False

    def size(self):
        return len(self.__queue)

if (__name__ == "__main__"):
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")
    q.enqueue(5)
    print(q.size())
    if(q.isEmpty()):
        print("Kön är tom")
    else:
        print("Kön är inte tom")
