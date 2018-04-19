from codagem.data_structure.delete_node_single_linked_list import LinkedListNode, delete_node

def test_delete_single_node_from_linked_list():
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')

    a.next = b
    b.next = c

    delete_node(b)

    assert a.next.value == 'C'
    assert c.next is None
