import unittest
from double_Linked_list import doubly_linked_list


def isEmpty_Test ():
    dll = doubly_linked_list()
    assert dll.isEmpty() == True,"your isempty method doesnt works"

def length_test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    assert dll.length() ,"length method doesnt works"

def search_test():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_end(10)
    assert dll.search(5) == True, "search method doesn't work"
    assert dll.search(10) == True, "search method doesn't work"
    assert dll.search(15) == False, "search method doesn't work"


def insert_at_Beginning_Test():
    dll = doubly_linked_list()  
    dll.insert_At_Beginning(5)
    assert dll.head.data == 5, "Insert at beginning doesn't work"


def insert_at_End_Test():
    dll = doubly_linked_list()  
    dll.insert_At_end(10)
    assert dll.head.data == 10, "Insert at end method doesn't work"

def insert_after_an_element():
    dll = doubly_linked_list()
    dll.insert_At_Beginning(5)
    dll.insert_At_end(10)
    dll.insert_At_end(15)
    dll.insert_After_Element(5,15)
    assert dll.head.next.data == 5 ,"insert after element method doesnt works "


if __name__==("__main__"):
    isEmpty_Test()
    length_test()
    search_test()
    insert_at_Beginning_Test()
    insert_at_End_Test()
