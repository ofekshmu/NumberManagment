from ByteNode import ByteNode

class LinkedListBinaryNum:

    def __init__(self, num: int):
        """ Class constructor - initialized the binary list """

        if not isinstance(num, int):
            raise TypeError("num is not of type int!")
        if num < 0:
            raise ValueError("num is not positive!")

        BYTE_SIZE = 8
        if num == 0:
            binary_padded = BYTE_SIZE*"0"
        else:
            binary_rep = bin(num)[2:]
            padding_size = (BYTE_SIZE - (len(binary_rep) % BYTE_SIZE)) % BYTE_SIZE
            binary_padded = padding_size*"0" + binary_rep

        msb_byte = binary_padded[:8]
        self.head = ByteNode(msb_byte)
        curr_node = self.head
        
        iter_count = len(binary_padded) // BYTE_SIZE - 1 
        for i in range(iter_count):
            byte = binary_padded[(i + 1)*BYTE_SIZE: (i + 1)*BYTE_SIZE + BYTE_SIZE]
            node = ByteNode(byte)
            curr_node.next = node
            curr_node = node
        
        curr_node.next = None

        self.size = len(binary_padded) // BYTE_SIZE

    def add_MSB(self, byte: str) -> None:
        """ Add an MSB ByteNode to the list """
        second_node = self.head
        self.head = ByteNode(byte)
        self.head.next = second_node
        self.size += 1


    def __repr__(self) -> str:
        """ return an str desribing the byte list """
        lst_repr = ""
        bn = self.head
        while bn is not None:
            lst_repr += bn.__repr__()
            bn = bn.next
        lst_repr += "None"
        
        s = ''
        if self.size > 1:
            s = 's'

        return f"LinkedListBinaryNum with {self.size} Byte{s}, Bytes map: {lst_repr}" 

    def __str__(self):
        """ """
        st = ""
        pos = self.head

        while pos is not None:
            st += f"|{pos.byte}"
            pos = pos.next
        
        return st + "|"
    
    def __len__(self):
        """ """
        return self.size

    def __getitem__(self, item):
        """ """
        if item >= self.size or item <= -self.size - 1:
            raise IndexError(f"Bad index!")

        if item < 0:
            item = item + self.size

        pos = self.head
        for i in range(item):
            pos = pos.next
        
        return pos.byte

    def __eq__(self, other):
        
        if not isinstance(other, LinkedListBinaryNum):
            raise TypeError("This is not a type LinkedListBinaryNum")

        if other.size != self.size:
            return False
        
        pos1 = self.head
        pos2 = other.head
        while pos1 != None:
            for i in range(8):
                if pos1.byte[i] != pos2.byte[i]:
                    return False
            pos1 = pos1.next
            pos2 = pos2.next

        return True

    def __add__(self, other):
        """ """
        pass

    def __radd__(self, other):
        """ """
        pass

    def __sub__(self, other):
        """ """
        pass
    
        
