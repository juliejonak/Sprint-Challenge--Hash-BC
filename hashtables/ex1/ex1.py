#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    if length < 2:
        return None

    # This solution does not account for resizing the hashtable if the length is >16.
    # Refactoring would include handling those edge cases
    
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)
    

    for i in range(0, length):
        complimentary_weight = limit - weights[i]

        if hash_table_retrieve(ht, complimentary_weight):
            if i > hash_table_retrieve(ht, complimentary_weight):
                return (i, hash_table_retrieve(ht, complimentary_weight))
            else:
                return (hash_table_retrieve(ht, complimentary_weight), i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
        return answer
    else:
        print("None")
