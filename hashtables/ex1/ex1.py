


def get_indices_of_item_weights(weights, length, limit):
    # instance of dictionary
    dictio = {}
# iterate over the list of weights
    for i, weight in enumerate(weights):
        # check if current weight is already in the dictionary
        if weight in dictio:
            # if current weight is in the dictionary,get its index by getting the value through the key of weight
            value = dictio[weight]
            # return current index and value(index in dictionary) wihtin tuple
            return (i, value)
            # if the weights arent in the dictionary,assign the difference key, the value of the current index
        else:
            diff = limit - weight
            dictio[diff] = i


