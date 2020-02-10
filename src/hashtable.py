# '''
# Linked List hash table key/value pair
# '''

import hashlib

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
        
        self.key = key.encode()
        
        return hash(self.key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        self.key = key
        hash_DJB2 = 5381
        for x in self.key:
            hash_DJB2 = (( hash_DJB2 << 5) + hash_DJB2) + ord(x)
        
        return hash_DJB2 & 0xFFFFFFFF
        
        


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        self.value = value
        self.key = key
        index = self._hash_mod(key)
        
        self.storage[index] = value
        
        return self.storage



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        self.key = key
        index = self._hash_mod(key)
        
        self.storage[index] = None
        
        return self.storage


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        self.key = key
        index = self._hash_mod(key)
        
        return self.storage[index]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        self.storage2 = [None] * self.capacity
        for i in self.storage:
            if i == None:
                continue
            hashed = self._hash_mod(i)
            self.storage2.insert(hashed, i)
        self.storage = self.storage2
        return self.storage



if __name__ == "__main__":
    example = HashTable(8)
    print(example._hash("some string"))
    print(example._hash_djb2("some string")) 
    print(example._hash_mod("some string"))
    print(example.insert("Name of string", "some string"))
    print(example.insert("Name of string 2", "some string 2"))
    print(example.retrieve("Name of string"))
    print(example.resize())
    print(example.remove("Name of string"))


    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

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
