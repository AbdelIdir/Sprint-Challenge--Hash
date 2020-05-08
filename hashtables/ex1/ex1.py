import sys

from hashtable import (HashTable,
                       hash_table_insert,
                       hash_table_remove,
                       hash_table_retrieve,
                       hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(8)

    for i in range(length):
        findindices = limit - weights[i]
        indicefound = hash_table_retrieve(ht, findindices)

        if indicefound == None:
            hash_table_insert(ht, weights[i], i)
        else:
            return max(indicefound, i), min(indicefound, i)

    return None
