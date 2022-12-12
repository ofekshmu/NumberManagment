from ByteNode import ByteNode

class LinkedListBinaryNum:

    def __init__(self, num: int):
        """ Class constructor - initialized the binary list """

        if not isinstance(num, int):
            raise TypeError("num is not of type int!")
        if num < 0:
            raise ValueError("num is not positive!")

        self.head = "?"
        self.size = "?"

    def add_MSB(self, byte: str) -> None:
        """ Add an MSB ByteNode to the list """
        pass

    def __repr__(self) -> str:
        """ return an str desribing the byte list """
        lst_repr = ""
        bn = self.head
        while bn is not None:
            lst_repr += bn.__repr__()
            bn = bn.next
        lst_repr += "None"
        return f"LinkedListBinaryNum with {self.size}, Bytes map: {lst_repr}" 