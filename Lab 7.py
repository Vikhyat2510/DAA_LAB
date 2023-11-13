#lab 7
class BinarySearchTreeNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return BinarySearchTreeNode(value)
    else:
        if root.value < value:
            root.right = insert_node(root.right, value)
        else:
            root.left = insert_node(root.left, value)
    return root

def search_node(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search_node(root.right, value)
    return search_node(root.left, value)


def build_binary_search_tree():
    root = None
    n = int(input("Enter the number of elements to insert into the Binary Search Tree: "))
    for _ in range(n):
        value = int(input("Enter a value: "))
        root = insert_node(root, value)
    return root


def search_binary_search_tree(root):
    search_value = int(input("Enter the value to search in the Binary Search Tree: "))
    result = search_node(root, search_value)
    if result:
        print(f"Node with value {search_value} found in the BST.")
    else:
        print(f"Node with value {search_value} not found in the BST.")


root = build_binary_search_tree()

search_binary_search_tree(root)



#lab 7
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leaf_node_sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.value

    left_sum = leaf_node_sum(root.left)
    right_sum = leaf_node_sum(root.right)

    return left_sum + right_sum

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

result = leaf_node_sum(root)

print(f"Sum of leaf nodes in the tree: {result}")





#lab 7

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def spiral_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]
    left_to_right = True

    while queue:
        level_values = []
        level_size = len(queue)

        for _ in range(level_size):
            if left_to_right:
                current_node = queue.pop(0)
                level_values.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            else:
                current_node = queue.pop()
                level_values.append(current_node.value)
                if current_node.right:
                    queue.insert(0, current_node.right)
                if current_node.left:
                    queue.insert(0, current_node.left)

        result.append(level_values)
        left_to_right = not left_to_right

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = spiral_order_traversal(root)

print("Spiral Order Traversal:")
for level in result:
    print(level)







