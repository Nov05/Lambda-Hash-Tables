# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # return hash(key)
        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        h = 5381
        for k in key:
            h = (( h << 5) + h) + ord(k)
        return h & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if node is None:
            self.storage[index] = LinkedPair(key, value)
            return

        while node:
            if node.key == key:
                node.value = value
                return
            if node.next is None:
                node.next = LinkedPair(key, value)   
            node = node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if node is None:
            print('Key is not found in the hash table.')
            return

        node_prev = None
        while node: 
            if node.key == key:
                if node_prev:
                    node_prev.next = node.next
                else:
                    self.storage[index] = node.next
                return
            node = node.next
        print('Key is not found in the hash table.')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        try:
            node = self.storage[self._hash_mod(key)]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
            return None
        except:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        storage_old = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for node in storage_old:
            self.insert(node.key, node.value)
            while node.next:
                node = node.next
                self.insert(node.key, node.value)  


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    # print(ht.storage[1].key)
    # print(ht.storage[0].key)
    # print(ht.storage[1].next.key)

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
