from ByteNode import ByteNode
from LinkedListBinaryNum import LinkedListBinaryNum

def test_byte_node():
    bn = ByteNode('10011000')
    assert bn.get_next() is None

    bn = ByteNode('10011000')
    assert bn.__repr__() == "[10011000]=>"
    bn2 = ByteNode('11111111')
    bn2.set_next(bn)
    assert bn2.get_next().get_byte() == "10011000"


def tests_init_linked_list_binary_num():
    bn1 = LinkedListBinaryNum(0)
    assert bn1.__repr__() == "LinkedListBinaryNum with 1 Byte, Bytes map: [00000000]=>None"
    bn1 = LinkedListBinaryNum(255)
    assert bn1.__repr__() == "LinkedListBinaryNum with 1 Byte, Bytes map: [11111111]=>None"
    bn1 = LinkedListBinaryNum(4294967296)
    assert bn1.__repr__() == "LinkedListBinaryNum with 5 Bytes, Bytes map: [00000001]=>[00000000]=>[00000000]=>[00000000]=>[00000000]=>None"
    for i in range(2**8 - 1):
        bn1 = LinkedListBinaryNum(i)
        assert bn1.__repr__() == f"LinkedListBinaryNum with 1 Byte, Bytes map: [{bin(i)[2:].zfill(8)}]=>None"
    
    for i in range(2**8, 2**16 - 1):
        bn1 = LinkedListBinaryNum(i)
        assert bn1.__repr__() == f"LinkedListBinaryNum with 2 Bytes, Bytes map: [{bin(i)[2:].zfill(16)[:8]}]=>[{bin(i)[2:].zfill(16)[8:]}]=>None"



tests_init_linked_list_binary_num()