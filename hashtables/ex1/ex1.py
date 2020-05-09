import sys

from hashtable import (HashTable,
                       hash_table_insert,
                       hash_table_remove,
                       hash_table_retrieve,
                       hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # instance of dictioanry
    dictio = {}
# iterate over the list of weights
    for i, weight in enumerate(weights):
        # check if current weight is already in the dictionary
        if weight in dictio:
            # if current weight is in the dictionary,get its index by getting the value through the key of weight
            value = dictio[weight]
            # return index and value wihtin tuple
            return (i, value)
            # if the weights arent in the dictionary,assign the difference key, the value of the current index
        else:
            diff = limit - weight
            dictio[diff] = i

# There is going to be a limit
# there is going to be a list of weights
# the goal is to find the indexes of two items summed together that would equal the limit
# the heaviest item should be placed first in the response
