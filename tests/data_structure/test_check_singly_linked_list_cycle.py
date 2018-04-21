#from codagem.data_structure.delete_node_single_linked_list import LinkedListNode, delete_node

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

def contains_cycle(head):
    node = head.next
    visited = set()
    while node != None:
        if node in visited:
            return True

        visited.add(node)
        node = node.next

    return False

def test_detect_cycle_singly_list_node_returns_true():
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')

    a.next = b
    b.next = c
    c.next = a

    assert contains_cycle(a) == True

def test_returns_false_when_linked_list_doesnt_have_cycle():
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')

    a.next = b
    b.next = c

    assert contains_cycle(a) == False
