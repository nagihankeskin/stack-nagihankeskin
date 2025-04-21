class LLNode:
    def __init__(self, node):
        self.node = node      # node object
        self.next = None  # sonraki node


class LinkedList:
    def __init__(self):
        self.head = None #listenin başı
        self.num_items = 0 #eleman sayısı

    def add_node(self, node, index):  #belirtilen indexe düğüm ekleme
        new_node = LLNode(node)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.num_items += 1

    def remove_node(self, index):   #belirtilen indexteki düğümü silme
        if self.head is None:
            return None

        if index == 0:
            removed_node = self.head
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            removed_node = current.next
            current.next = current.next.next

        self.num_items -= 1
        return removed_node.node

class Stack:
    def __init__(self):
        self.top = LinkedList() 

    def push(self, node):   #en üste eleman ekle
        self.top.add_node(node, 0)  #en başa ekle

    def pop(self):   #en üstteki elemanı sil
        return self.top.remove_node(0) #en baştan sil

    def peek(self):  #en üstteki elemanı göster 
        if self.top.head:
            return self.top.head.node
        return None
