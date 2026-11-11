class Node:
    def __init__(self, key = 0, val= 0, next =None, prev= None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.lib = {}
        self.start_node = Node()
        self.end_node = Node()
        self.start_node.next = self.end_node
        self.end_node.prev = self.start_node
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.lib:
            return -1
        
        self.use(self.lib[key])
        self.insert(self.lib[key])
        return self.lib[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.lib:
            self.use(self.lib[key])
            self.insert(self.lib[key])
            self.lib[key].val = value
        else:
            new_node = Node(val = value, key = key)
            self.insert(new_node)
            self.lib[key] = new_node
            if len(self.lib) > self.capacity:
                delete_node = self.start_node.next
                second_node = self.start_node.next.next
                self.start_node.next = second_node
                second_node.prev = self.start_node
                del self.lib[delete_node.key]


    def use(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):

        last_node = self.end_node.prev
        last_node.next = node
        node.prev = last_node
        self.end_node.prev = node
        node.next = self.end_node
        
