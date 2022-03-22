def hashmap_left_join(table_left, table_right):
    for key in table_left.keys():
        table_left.set(key, [table_left.get(key), table_right.get(key)])

