def left_join(hashtable_a, hashtable_b):
    whole_table = []

    for key in hashtable_a:
        whole_table.append(key)
        whole_table.append(hashtable_a[key])

        if key in hashtable_b:
            whole_table.append(hashtable_b[key])
        else:
            whole_table.append(None)
    return whole_table
