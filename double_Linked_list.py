class Node :
    def __init__(self,value):
        self.previous = None
        self.data = value
        self.next = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

    def insert_At_Beginning(self,value):
            new_node = Node(value)
            if self.isEmpty():
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node


    def insert_At_end(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.insert_At_Beginning(value)
        else :
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp


    def insert_After_Element(self,value,element):
        temp = self.head
        while temp != None:
            if temp.data == element:
                break
            temp = temp.next
        if temp == None:
            print("element not found ")
        else :
            new_node = Node(value)
            new_node.next = temp.next
            new_node.previous = temp
            temp.next.previous = new_node
            temp.next = new_node


    def isEmpty(self):
        if self.head is None :
            return True
        return False
    

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            temp = temp.next
            count +=1
        return count


    def search(self,value):
        temp = self.head
        isFound = False
        while temp != None :
            if temp.data == value:
                isFound = True
                break
            temp = temp.next
        return isFound


    
        