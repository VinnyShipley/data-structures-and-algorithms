from data_structures.hashtable import Hashtable

def left_join(table_a, table_b):

    return_table = []
    a_keys = table_a.keys()

    for key in a_keys:

        if table_b.contains(key):
            return_table.append([key, table_a.get(key), table_b.get(key)])

        else:
            return_table.append([key, table_a.get(key), None])

    return return_table
