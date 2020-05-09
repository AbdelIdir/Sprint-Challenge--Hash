


class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


def hash(x, storageability):

    hash = 5381
    for char in x:
        hash = ((hash << 5) + hash) + ord(char)
        return hash % storageability



def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))

    current_node = hash_table.storage[index]
    last_node = None

    while current_node is not None and current_node.key != key:
        last_node = current_node
        current_node = last_node.next

    if current_node is not None:
        current_node.value = value
    else:
        new_node = HashTableEntry(key, value)
        new_node.next = hash_table.storage[index]
        hash_table.storage[index] = new_node


def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_node = hash_table.storage[index]
    last_node = None

    while current_node is not None and current_node.key != key:
        last_node = current_node
        current_node = last_node.next

    if current_node is None:
        print("No entry to be removed")
    else:
        if last_node is None:  
            hash_table.storage[index] = current_node.next
        else:
            last_node.next = current_node.next


def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_node = hash_table.storage[index]

    while current_node is not None:
        if(current_node.key == key):
            return current_node.value
        current_node = current_node.next


def hash_table_resize(hash_table):
    new_hash_table = HashTable(2 * len(hash_table.storage))

    current_node = None

    for i in range(len(hash_table.storage)):
        current_node = hash_table.storage[i]
        while current_node is not None:
            hash_table_insert(new_hash_table,
                              current_node.key,
                              current_node.value)
            current_node = current_node.next

    return new_hash_table
