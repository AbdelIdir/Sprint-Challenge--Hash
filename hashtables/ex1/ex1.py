import sys

from hashtable import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
	ht = HashTable(16)

	for i in range(length):
		looking = limit - weights[i]
		found = hash_table_retrieve(ht, looking)

		if found == None:
			hash_table_insert(ht, weights[i], i)
		else:
			return max(found, i), min(found, i)

	return None


#d
