def h_index(citations):
    h = 0
    for i in range(citations):
        if citations[i] >= citations[i] + 1:
            h = i + 1
        else:
            break
    return h
