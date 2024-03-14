class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.head = Node('head')

    def __str__(self):
        cur = self.head.next
        out = ''
        sep = ' => '
        while cur != None:
            out += f"{cur.value}{sep}"
            cur = cur.next
        out = out[:-4]
        return out

    def push(self, value):
        new_element = Node(value)
        new_element.next = self.head.next
        self.head.next = new_element

    def pop(self):
        tmp = self.head.next.value
        self.head.next = self.head.next.next
        return tmp


class PersistentStack(Stack):
    def __init__(self):
        self.backups = []
        super().__init__()

    def backup(self):
        self.backups.append(self.__str__())

    def get_backup(self, i):
        return self.backups[i]

    def push(self, value):
        self.backup()
        super().push(value)

    def pop(self):
        self.backup()
        super().pop()