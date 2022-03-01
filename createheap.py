def heappop(nodeArray):
    leng = len (nodeArray)
    smallest = nodeArray[0].freq
    key = 0
    for i in range (leng):
        if nodeArray[i].freq < smallest:
            smallest = nodeArray[i].freq
            key = i
    ret_node = nodeArray[key]
    nodeArray.remove(nodeArray[key])
    return ret_node

def returnRootNode (nodeArray):
    leng = len (nodeArray)
    largest = nodeArray[0].freq
    key = 0
    for i in range (leng):
        if nodeArray[i].freq > largest:
            largest = nodeArray[i].freq
            key = i
    return (nodeArray[key])

def heappush (nodeArray, node):
    nodeArray.append(node)

    
            