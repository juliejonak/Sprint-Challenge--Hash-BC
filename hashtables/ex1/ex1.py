#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    if length < 2:
        return None

    # This solution does not account for resizing the hashtable if the length is >16.
    # Refactoring would include handling those edge cases
    
    # sets up a hashtable with each weight as the key and the index as the value
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)
    

    for i in range(0, length):
        # finds what the complimentary weight would be for item i
        complimentary_weight = limit - weights[i]

        # if complimentary weight exists
        if hash_table_retrieve(ht, complimentary_weight):
            # if i is the greater value, returns it as the first item in the tuple
            if i > hash_table_retrieve(ht, complimentary_weight):
                return (i, hash_table_retrieve(ht, complimentary_weight))
            # else if i is the lower value, returns it as the second item in the tuple
            else:
                return (hash_table_retrieve(ht, complimentary_weight), i)

    # if the key doesn't exist, returns None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
        return answer
    else:
        print("None")
