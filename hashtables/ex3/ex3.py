def intersection(arrays):

    dictio = {}
    for element in arrays:
        for el in element:
            if dictio.get(el) == None:
                ## if the element is not in the dictionary, we return 0, since there will not be any number found.
                dictio[el] = 0
                ## we increment the index, and keep looking
            dictio[el] = dictio.get(el) + 1
## we return the elements that are present in all arrays
    result = [element for element, el in dictio.items() if el == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
