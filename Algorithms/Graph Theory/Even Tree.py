#https://www.hackerrank.com/challenges/even-tree

def find_tree_size(node,edge_list):
    #get the size of the tree from this node down
    all_children_found = False
    tree_list = [node]
    while not all_children_found:
        new_additions = 0
        for i in range(len(tree_list)): #go through all the nodes in the tree list
            this_node = tree_list[i]
            for i in range(len(edge_list)): #find all the children to each node in the tree list
                if edge_list[i][1] == this_node:
                    child_node = edge_list[i][0] #the child node
                    if not child_node in tree_list: #if the child node isn't already in the list
                        tree_list.append(child_node); #add the new node to the tree list
                        new_additions += 1
        if new_additions == 0: #if no new nodes have been added to the tree list, then all the children have been found
            all_children_found = True
    return(len(tree_list))

def find_tree_tops(node_count,edge_list):
    tree_tops = []
    #If a node doesn't point to any other nodes, add it to the tree top list
    for i in range(1,node_count+1):
        found = False
        for j in range(len(edge_list)):
            if edge_list[j][0] == i:
                found = True
        if not found:
            tree_tops.append(i)
    return(tree_tops)


a = [int(i) for i in input().strip().split(' ')]
node_count = a[0]
edge_count = a[1]
edge_list = [[int(i) for i in input().strip().split(' ')] for j in range(edge_count)]

answer = False
counter = 0
node_list = []
for i in range(1,node_count+1):
    node_list.append(i)
    
while True:        
    smallest_tree = -1
    smallest_tree_node = 0
    for i in range(len(node_list)):
        node = node_list[i]
        tree_size = find_tree_size(node,edge_list)
        if tree_size%2 == 0: #if the tree size is even
            if smallest_tree == -1:
                smallest_tree = tree_size
                smallest_tree_node = node
            elif tree_size < smallest_tree:
                smallest_tree = tree_size
                smallest_tree_node = node
                
    if smallest_tree_node == 1: #if the smallest even tree left in the node list is the tree that starts with "1"
        break
    
    #Remove node from node list
    node_to_pop = -1
    for i in range(len(node_list)):
        if node_list[i] == smallest_tree_node:
            node_to_pop = i
            counter += 1
    if node_to_pop > 0:
        node_list.pop(node_to_pop)
        
    #Remove the edge from tree list
    edge_to_pop = -1
    for i in range(len(edge_list)):
        if edge_list[i][0] == smallest_tree_node:
            edge_to_pop = i
    if edge_to_pop > 0:
        edge_list.pop(edge_to_pop)
    
print(counter)