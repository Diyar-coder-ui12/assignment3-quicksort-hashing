

# ---------------------------
# Hash Table with Chaining
# ---------------------------

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
        else:
            # Update if key exists
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev = node
                node = node.next
            prev.next = Node(key, value)
        self.size += 1
        if self.size / self.capacity > 0.7:  # Load factor threshold
            self._resize()

    def search(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for node in old_table:
            while node:
                self.insert(node.key, node.value)
                node = node.next


# ---------------------------
# Example usage
# ---------------------------

if __name__ == "__main__":
    ht = HashTable()
    ht.insert("Alice", 25)
    ht.insert("Bob", 30)
    ht.insert("Charlie", 35)

    print("Search Bob:", ht.search("Bob"))
    print("Delete Alice:", ht.delete("Alice"))
    print("Search Alice:", ht.search("Alice"))



