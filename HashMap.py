class ChainingHash:
    # __init__ method: O(n), where n is the initial capacity
    def __init__(self, initial_capacity=20):
        # Initialize the hash table with a list of empty buckets
        self.bucket_list = []
        for i in range(initial_capacity):
            self.bucket_list.append([])

    # Inserts a new item into the hash table
    def insert(self, key, value):
        # Calculate the bucket index using the hash of the key
        bucket_index = hash(key) % len(self.bucket_list)
        bucket = self.bucket_list[bucket_index]

        # Check if the key already exists in the bucket
        for kv in bucket:
            if kv[0] == key:
                # Update the value if the key exists
                kv[1] = value
                return True

        # If the key doesn't exist, add a new key-value pair to the bucket
        key_value = [key, value]
        bucket.append(key_value)
        return True

    # Search for an item based on its key
    def search(self, key):
        # Calculate the bucket index using the hash of the key
        bucket_index = hash(key) % len(self.bucket_list)
        bucket = self.bucket_list[bucket_index]

        # Iterate through the key-value pairs in the bucket
        for pair in bucket:
            if key == pair[0]:
                # Return the value if the key matches
                return pair[1]
        # Return None if the key is not found
        return None

    # Remove an item from the hash table based on its key
    def hash_remove(self, key):
        bucket_index = hash(key) % len(self.bucket_list)
        bucket = self.bucket_list[bucket_index]

        # Check if the key is present in the bucket
        for pair in bucket:
            if key == pair[0]:
                bucket.remove(pair)
                return True
        return False

# the average time complexity for insert, search, and hash_remove methods is O(1) under the assumption of a good hash function and uniform distribution of keys.
# However, due to potential hash collisions, these methods can degrade to O(n) in the worst case scenario where all keys hash to the same bucket.
