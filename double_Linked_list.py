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


    def insert_After_Element(self, value, element):
        temp = self.head
        while temp is not None:
            if temp.data == element:
                break
            temp = temp.next
        if temp is None:
            print("Element not found")
        else:
            new_node = Node(value)
            new_node.next = temp.next
            if temp.next is not None:
                temp.next.previous = new_node
            new_node.previous = temp
            temp.next = new_node

    def insert_At_Position(self, value, pos):
        temp = self.head
        count = 0
        while temp is not None:
            if count == pos - 1:
                break
            count += 1
            temp = temp.next
        if pos == 1:
            self.insert_At_Beginning(value)
        elif temp is None:
            print("cannot add element here")
        elif temp.next is None:
            self.insert_At_end(value)
        else:
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


    def printLinkedLst(self):
        temp = self.head
        while temp != None :
            print(temp.data , end=" <--> ")
            temp = temp.next
        print("None")
    
    def updateElement(self,oldval , newval):
        temp = self.head
        isUpdate = False
        while temp != None : 
            if temp.data == oldval:
                temp.data = newval
                isUpdate = True
            temp = temp.next

    def updateAtPosition(self,value,pos):

        temp = self.head
        count = 0
        while temp != None:
            if count == pos:
                break
            count +=1
            temp = temp.next
        if temp is None :
            print("cannot update")
        else :
            temp.data = value
            print ("value updated")


    def deleteFromBeginnig(self):
        if self.head is None:
            print("linked list is empty")
        elif self.head.next is None :
            self.head = None
        else :
            self.head = self.head.next
            self.head.previous = None
