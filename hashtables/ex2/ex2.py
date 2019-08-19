#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Creates hashtable with key (source) and value (destination)
    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    # Finds the starting destination to place at beginning of route
    route[0] = (hash_table_retrieve(hashtable, "NONE"))

    # Finds next destination for each previous source and appends to route
    for i in range(1, length):
        source = route[i-1]
        route[i] = hash_table_retrieve(hashtable, str(source))

    return route
