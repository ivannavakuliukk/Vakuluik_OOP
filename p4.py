# first parameter is volume, second - weights
stuffdict = {'w1':(10, 1),
             'w2':(15, 3),
             'w3':(12, 2.3),
             'w4':(8, 0.7),
             'w5':(11, 1.5),
             'w6':(10,1),
             'w7':(7, 3)}
def get_volume_and_weights(stuffdict):
    capacity = [stuffdict[item][0] for item in stuffdict]
    weights = [stuffdict[item][1] for item in stuffdict]
    return capacity, weights

def get_memtable(stuffdict, C=30):
    capacity, weights = get_volume_and_weights(stuffdict)
    n = len(weights)  # find the size of the table

    # create a table with zero values
    V = [[0 for a in range(C + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for c in range(C + 1):
            # base case
            if i == 0 or c == 0:
                V[i][c] = 0

            # if the capacity of the item is less than the volume of the column,
            # maximize the total weights
            elif capacity[i - 1] <= c:
                V[i][c] = max(weights[i - 1] + V[i - 1][c - capacity[i - 1]], V[i - 1][c])

            # if the capacity of the item is larger than the capacity of the column,
            # take the cell weights from the previous row
            else:
                V[i][c] = V[i - 1][c]
    return V, capacity, weights

def get_selected_items_list(stuffdict, C = 30):
    V, capacity, weights = get_memtable(stuffdict)
    n = len(weights)
    res = V[n][C]  # start at the last element of the table
    c = C  # initial capacity - maximum
    items_list = []  # list of capacity and weights
    Weights = 0 # maximum weight of gold that fits into a knapsack with capacity of C
    for i in range(n, 0, -1):  # go in reverse order
        if res <= 0:  # interruption condition - assembled "backpack"
            break
        if res == V[i - 1][c]:  # do nothing, move on
            continue
        else:
            # "pick up" the item
            items_list.append((capacity[i - 1], weights[i - 1]))
            res -= weights[i - 1]  # subtract the weights of the weights from the total
            c -= capacity[i - 1]  # subtract the capacity from the total
            Weights += weights[i-1]

    selected_stuff = []

    # find the keys of the source dictionary - the names of the items
    for search in items_list:
        for key, weights in stuffdict.items():
            if weights == search:
                selected_stuff.append(key)

    return selected_stuff, Weights

stuff = get_selected_items_list(stuffdict)
print(stuff)
