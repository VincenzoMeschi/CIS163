from node import Node


class LLStack:
    """
    Linked list based stack class.

    Attributes
    ----------
    __head : Node
        Head node in the linked list.
    __size : int
        Number of elements in the stack.
    """

    def __init__(self):
        """
        Constructor for LLStack.
        """

        self.__head = None
        self.__size = 0

    @property
    def size(self) -> int:
        """
        Size property for LLStack.

        Returns
        ----------
        int
            Number of elements in the stack.
        """

        return self.__size

    def pop(self) -> tuple:
        """
        Removes the top node on the stack and returns the data (tuple) stored at that node.

        Returns
        ----------
        tuple
            Data stored at the top node in the stack.
        """

        if self.__size == 0:
            raise IndexError("pop from empty stack")

        data = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1

        return data

    def push(self, data: tuple):
        """
        Add a new node to the top of the stack.

        Parameters
        ----------
        data : tuple
            Tuple to be stored in the new node.

        Raises
        ----------
        TypeError
            If data is not a tuple containing integers.
        """

        if not isinstance(data, tuple) or not all(isinstance(i, int) for i in data):
            raise TypeError("data must be a tuple containing integers")

        self.__head = Node(data, self.__head)
        self.__size += 1

    def peek(self) -> tuple:
        """
        Returns the data (tuple) stored at the top node in the stack without removing it.

        Returns
        ----------
        tuple
            Data stored at the top node in the stack.
        """

        if self.__size == 0:
            raise IndexError("peek from empty stack")

        return self.__head.data

    def __str__(self) -> str:
        """
        String representation of LLStack.

        Returns
        ----------
        str
            String representation of the stack.
        """

        if self.__size == 0:
            return ""

        current = self.__head
        stack_str = str(current)

        while current.next is not None:
            current = current.next
            stack_str += f" -> {current}"

        return stack_str
