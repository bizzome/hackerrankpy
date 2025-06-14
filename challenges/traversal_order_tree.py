'''
    The idea is to traverse the tree recursively,
    passing the current node and its level, starting
    with the root at level 0. For each visited node,
    its value is added to the result array,
    considering the value of level as its index in
    the result array.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse_tree_recursively(node, level, result_array):
    if not node:
        return
    
    # if node level is 3, array must add the 3rd element
    if len(result_array) <= level:
        result_array.append([])

    result_array[level].append(node.value)

    traverse_tree_recursively(node.left, level + 1, result_array)
    traverse_tree_recursively(node.right, level + 1, result_array)
    print(result_array)


def levelOrder(root):
    res = []
    traverse_tree_recursively(root, 0, res)
    return res

if __name__ == "__main__":
    # Create binary tree
      #      1         
    #     / \       
    #    3   2      
    #          \   
    #           4 
    #          /  \
    #         6    5
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.right.right = Node(4)
    root.right.right.left = Node(6)
    root.right.right.right = Node(5)

    # Perform level order traversal
    res = levelOrder(root)

    # Print the result
    for level in res:
        for data in level:
            print(data, end=" ")