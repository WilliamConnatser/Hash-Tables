

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = (hash * 33) + ord(char)
    return hash % max

# If you are overwriting a value with a different key, print a warning.
# '''

# Stretch Resizing:
# If load factor > 150%
# then double size of hash table
# round up to next prime
# and rehash the values
def hash_table_insert(hash_table, key, value):
    index = hash(key,hash_table.capacity)
    if hash_table.storage[index]:
        print(f"Overwriting {key}")
    hash_table.storage[index] = value

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key,hash_table.capacity)
    if not hash_table.storage[index]:
        print(f"{key} doesn't exist")
    else:
        hash_table.storage[index] = None

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key,hash_table.capacity)
    if not hash_table.storage[index]:
        return None
    else:
        return hash_table.storage[index]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
