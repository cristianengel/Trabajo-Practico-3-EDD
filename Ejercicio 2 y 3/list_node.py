
class ListNode:
    
    __slots__ = "element", "next"
    
    def __init__(self, element : None, next = None) -> None:
        self.element = element
        self.next = next