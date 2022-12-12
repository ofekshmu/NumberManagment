from typing import Union, Type

class ByteNode:

    def __init__(self, byte: str):
        """ Constructor function """
        if not isinstance(byte, str):
            raise TypeError("input argument 'byte' is not op type string!")
        if len(byte) != 8:
            raise ValueError("input strin 'byte' is not of length 8!")
        self.byte = byte
        self.next = None

    def get_byte(self) -> str:
        """ get the byte field """
        return self.byte

    def get_next(self) -> Union[None, ByteNode]:
        """ get the next field """
        return self.next

    def __repr__(self) -> str:
        """ Describe Byte node using this string [byte]=> """
        return f"[{self.byte}]=>"