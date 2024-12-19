
# Creating a node class
class ItemSlot:
    def __init__(self, arrow, slotNum): # 'arrow' is an arrow object
        self.CURRENT_ARROW = arrow
        self.slotNum = slotNum

        self.RIGHT = None
        self.LEFT = None


# Creates a Doubly-LinkedList class:
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, arrow, slotNum):
        if self.head is None:
            newItemSlot = ItemSlot(arrow, slotNum)
            newItemSlot.LEFT = None
            self.head = newItemSlot
        else:
            newItemSlot = ItemSlot(arrow, slotNum)
            cur = self.head
            while cur.RIGHT:
                cur = cur.RIGHT
            cur.RIGHT = newItemSlot
            newItemSlot.LEFT = cur
            newItemSlot.RIGHT = None

    def printList(self):
        cur = self.head
        while cur:
            a = cur.CURRENT_ARROW
            print(a.arrowName)
            cur = cur.RIGHT

    def updateArrow(self, slotNum, selectedArrow):
        cur = self.head
        while cur:
            if cur.slotNum == slotNum:
                cur.CURRENT_ARROW = selectedArrow
            cur = cur.RIGHT


