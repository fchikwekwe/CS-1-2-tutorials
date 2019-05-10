""" This class creates a HashTable that can be used modularly in other files
n = key-value entries in HashTable
b = number of buckets
l = nodes in each bucket (LinkedList)"""

from linkedlist import LinkedList

class HashTable(object):
    """ This class creates a working hashtable that can be used
    in other projects"""

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running Time: O(n) because you would need to traverse all buckets and
        all keys within"""
        # Collect all keys in each bucket
        keys_list = []
        for bucket in self.buckets:
            # print(bucket)
            for key, _ in bucket.items():
                keys_list.append(key)
        return keys_list

    def values(self):
        """Return a list of all values in this hash table.
        Running Time: O(n) because you would need to traverse all buckets and
        all values within"""
        values_list = []
        # Loop through all buckets
        for bucket in self.buckets:
            for _, value in bucket.items():
                # Collect all values in each bucket
                values_list.append(value)
        return values_list

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) because you must traverse all buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) because you must traverse all buckets and all
        keys within buckets to get the length of each; if you use the .size
        property, then it would be O(b)"""
        count = 0
        # Loop through all buckets
        for bucket in self.buckets:
            for key in bucket.items():
                # Count number of key-value entries in each bucket
                count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: Best case O(1) if given key is the first item
        the first bucket; Worse case O(l) You need to traverse all buckets and
        the found bucket for key"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        print("bucket #:", bucket_index)
        bucket = self.buckets[bucket_index]
        # if key-value entry exists in bucket, then return True
        # using lambda function to get inside inner tuple
        pair = bucket.find(lambda tuple: tuple[0] == key)
        if pair:
            return True
        # else False
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: Best case O(1) if given key is the first item
        the first bucket; Worse case O(l) You need to traverse all buckets and
        the found bucket for key"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        print("bucket: {}".format(bucket))

        # Check if key-value entry exists in bucket
        pair = bucket.find(lambda tuple: tuple[0] == key)
        if pair:
            # If found, return value associated with given key
            return pair[1] # this is the value
        # Otherwise, raise error
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: Best case O(1) if given key is the first item
        the first bucket; Worse case O(l) You need to traverse all buckets and
        the found bucket for key"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        # Check if key-value entry exists in bucket
        pair = bucket.find(lambda tuple: tuple[0] == key)
        if pair:
            # If found, update value associated with given key
            bucket.delete(pair)
        # Otherwise, insert given key-value entry into bucket
        bucket.append((key, value))
        print("bucket: {}".format(bucket))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: Best case O(1) if given key is the first item
        the first bucket; Worse case O(l) You need to traverse all buckets and
        the found bucket for key"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        # Check if key-value entry exists in bucket
        pair = bucket.find(lambda tuple: tuple[0] == key)
        # If found, delete entry associated with given key
        if pair:
            bucket.delete(pair)
        # Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    """ tests implemented hashtable """
    test_hashtable = HashTable()
    print('hash table: {}'.format(test_hashtable))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        test_hashtable.set(key, value)
        print('hash table: {}'.format(test_hashtable))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = test_hashtable.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', test_hashtable.contains('X')))
    print('length: {}'.format(test_hashtable.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            test_hashtable.delete(key)
            print('hash table: {}'.format(test_hashtable))

        print('contains(X): {}'.format(test_hashtable.contains('X')))
        print('length: {}'.format(test_hashtable.length()))


if __name__ == '__main__':
    test_hash_table()
