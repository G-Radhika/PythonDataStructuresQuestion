'''
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
'''
#!/usr/local/bin/python

head = None


class NodeTree(object):
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None


'''
Function to insert a new node at the beginning
'''


def push_right(node, new_data):
    new_node = NodeTree(new_data)
    node.right = new_node
    return new_node


'''
Function to insert a new node at the beginning
'''


def push_left(node, new_data):
    new_node = NodeTree(new_data)
    node.left = new_node
    return new_node


'''
Function to find LCA of n1 and n2. The function assumes
that both n1 and n2 are present in BST
'''


def lca(head, n1, n2):
    # Base Case
    if head is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(head.data > n1 and head.data > n2):
        return lca(head.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(head.data < n1 and head.data < n2):
        return lca(head.right, n1, n2)

    return head.data


'''
Reconsider your space complexity. Whenever you make a function call,
the call stack stores the place where it's coming from. So, if you make
k recursive calls, the space complexity is O(k). Here is a link that discusses it:
http://stackoverflow.com/questions/10821059/space-complexity-of-recursive-algorithm.

You can avoid this recursive overhead by doing an iterative approach,
meaning do a simple while loop instead of recursion.
'''


def LCA_tree(mat, root, n1, n2):
    global head
    # Make BST
    head = Node(root)
    
#When you create a BST you are consuming O(n) space (one object for each node)
# and it takes O(n^2) time to compute. The biggest benefit of doing this is so
# that you can do operations like node.right and node.left, but doing this is
# unnecessary and can be avoided. Instead, simply use T as its given. I suggest
# creating functions like: get_right_child(tree, node) instead of using
# node.right, for example.
    
    head.left, head.right = None, None
    node_value = 0
    node_list = []
    for elem in mat[root]:
        if elem:
            if(node_value > root):
                node_list.append(push_right(head, node_value))
            else:
                node_list.append(push_left(head, node_value))
        node_value += 1

    tmp_node = node_list.pop(0)
    while tmp_node != None:
        node_value = 0
        for elem in mat[tmp_node.data]:
            if elem:
                if(node_value > tmp_node.data):
                    node_list.append(push_right(tmp_node, node_value))
                else:
                    node_list.append(push_left(tmp_node, node_value))
            node_value += 1
        if node_list == []:
            break
        else:
            tmp_node = node_list.pop(0)

    return lca(head, n1, n2)


def main():

  global head
  print LCA_tree([[0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1],
                  [0, 0, 0, 0, 0]],
                 3, 1, 2)


if __name__ == '__main__':
    main()
