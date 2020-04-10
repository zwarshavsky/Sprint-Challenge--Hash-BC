#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for wt in weights:
        hash_table_insert(ht,wt,weights.index(wt))
    # limit - wt
    for wt in weights:
        if hash_table_retrieve(ht,(limit-wt)) is not None:
            if wt == (limit-wt):
                return (weights.index(wt,weights.index(wt)+1),weights.index(wt))
            zero=max([wt,(limit-wt)])
            one=min([wt,(limit-wt)])
            return (hash_table_retrieve(ht,zero),hash_table_retrieve(ht,one))
            

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
