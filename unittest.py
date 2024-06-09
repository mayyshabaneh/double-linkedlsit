import unittest
from double_Linked_list import doubly_linked_list
def isEmpty_Test ():
    dll = doubly_linked_list()
    assert dll.isEmpty() == True,"your isempty method doesnt works"

def length_test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    assert dll.length() ,"length method doesnt works"
    dll.printLinkedLst()

def search_test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_end(10)
    assert dll.search(5) == True, "search method doesn't work"
    assert dll.search(10) == True, "search method doesn't work"
    assert dll.search(15) == False, "search method doesn't work"
    dll.printLinkedLst()


def insert_at_Beginning_Test():
    dll = doubly_linked_list()  
    dll.insert_At_Beginning(5)
    assert dll.head.data == 5, "Insert at beginning doesn't work"
    dll.printLinkedLst()


def insert_at_End_Test():
    dll = doubly_linked_list()  
    dll.insert_At_end(10)
    assert dll.head.data == 10, "Insert at end method doesn't work"
    dll.printLinkedLst()

def insert_after_an_element_Test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_end(10)
    dll.insert_At_end(15)
    dll.insert_After_Element(5, 10)
    assert dll.head.next.data == 10, "Insert after element method doesn't work"
    dll.printLinkedLst()

def insert_at_position_Test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_Beginning(6)
    dll.insert_At_end(20)
    dll.insert_At_end(30)
    dll.insert_At_Position(40, 1)
    assert dll.head.data == 40, "insertion method doesn't work"
    dll.printLinkedLst()


def update_val_Test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_Beginning(6)
    dll.insert_At_Beginning(7)
    dll.insert_At_Beginning(8)
    dll.insert_At_Beginning(9)
    dll.insert_At_Beginning(5)
    dll.insert_At_Beginning(6)
    dll.insert_At_Beginning(10)
    dll.insert_At_Beginning(11)
    dll.insert_At_Beginning(12)
    dll.insert_At_Beginning(13)
    dll.printLinkedLst()
    dll.updateElement(12,100)
    dll.updateElement(13,200)
    dll.printLinkedLst()
    assert dll.search(100) == True , "update field"
    assert dll.search(200) == True , "update field"

def update_val_atPos_Test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_Beginning(6)
    dll.insert_At_Beginning(7)
    dll.insert_At_Beginning(8)
    dll.insert_At_Beginning(9)
    dll.insert_At_Beginning(5)
    dll.insert_At_Beginning(6)
    dll.insert_At_Beginning(10)
    dll.insert_At_Beginning(11)
    dll.insert_At_Beginning(12)
    dll.insert_At_Beginning(13)
    dll.printLinkedLst()
    dll.updateAtPosition(200,5)
    dll.printLinkedLst()
    assert dll.search(200) == True , "update field"


def delete_from_beginnig():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_Beginning(6)
    dll.insert_At_Beginning(7)
    dll.insert_At_Beginning(13)
    dll.printLinkedLst()
    dll.deleteFromBeginnig()
    assert dll.search(13) == False , "delete field"
    dll.printLinkedLst()

isEmpty_Test()
length_test()
search_test()
insert_at_Beginning_Test()
insert_at_End_Test()
insert_after_an_element_Test()
insert_at_position_Test()
update_val_Test()
update_val_atPos_Test()
delete_from_beginnig()