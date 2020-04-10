#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    for ticket in tickets:
        print(hashtable,ticket.source,ticket.destination)
        hash_table_insert(hashtable,ticket.source,ticket.destination)
        
    node = hash_table_retrieve(hashtable,"NONE")
    # print(node)
    while(node != "NONE"):
        route.append(node)
        node = hash_table_retrieve(hashtable,node)
        
    return route


if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")
    tickets = [ticket_1,ticket_2,ticket_3]
    length = 3
    print(reconstruct_trip(tickets, length))
