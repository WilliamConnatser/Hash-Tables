

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = (hash * 33) + ord(char)
    return hash % max

# '''
# Insert into hash table
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key,hash_table.capacity)
    if hash_table.storage[index]:
        current_pair = hash_table.storage[index]
        while current_pair.next and current_pair.key != key:
            current_pair= current_pair.next
        if(current_pair.key == key):
            current_pair.value = value
        else:
            current_pair.next = LinkedPair(key,value)
    else:
        hash_table.storage[index] = LinkedPair(key,value)


# '''
# Remove From Hash Table
# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key,hash_table.capacity)
    if hash_table.storage[index]:
        current_pair = hash_table.storage[index]
        removed = None
        if current_pair.key == key:
            removed = current_pair
            hash_table.storage[index] = current_pair.next
        else:
            while current_pair.next and current_pair.next.key != key:
                current_pair = current_pair.next
            if current_pair.next:
                removed = current_pair.next
                current_pair.next = current_pair.next.next
            else:
                print("That does not exist")
                return None                
        return removed.value
    else:
        print("That does not exist")
        return None


# '''
# Retrieve A Value
# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key,hash_table.capacity)
    if hash_table.storage[index]:
        current_pair = hash_table.storage[index]
        while current_pair.next and current_pair.key != key:
            current_pair = current_pair.next
        if current_pair.key == key:
            return current_pair.value
        else:
            print("That does not exist")
            return None
    else:
        print("That does not exist")
        return None


# '''
# Resize Table
# Returns resized and re-keyed HT
# '''
def hash_table_resize(hash_table):
    new_ht = HashTable(hash_table.capacity * 2)

    for item in hash_table.storage:
        if item:
            current_item = item
            hash_table_insert(new_ht,current_item.key,current_item.value)
            while current_item.next:
                current_item = current_item.next
                hash_table_insert(new_ht,current_item.key,current_item.value)
    return new_ht

def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
