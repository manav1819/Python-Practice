'''
This programs draws a tree based on 

N_O_T_E: https://pygraphviz.github.io/documentation/stable/install.html 
Follow steps in this link to install pygraphviz
'''
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_value = preorder.pop(0)
    root = TreeNode(root_value)
    inorder_index = inorder.index(root_value)

    root.left = build_tree(preorder, inorder[:inorder_index])
    root.right = build_tree(preorder, inorder[inorder_index + 1:])

    return root

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value, end=" ")
        print_inorder(root.right)

def visualize_tree(root):
    G = nx.DiGraph()

    def add_edges(node, G, pos, x, y, layer):
        if node:
            G.add_node(node.value, pos=(x, y))
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_edges(node.left, G, pos, x - 2 ** (layer + 1), y - 1, layer + 1)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_edges(node.right, G, pos, x + 2 ** (layer + 1), y - 1, layer + 1)

    add_edges(root, G, None, 0, 0, 0)

    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
    plt.show()

# Example usage:
preorder = [17, 43, 12, 36, 9, 18, 2, 16, 19, 21, 3, 8]
inorder = [36, 12, 9, 43, 2, 18, 16, 17, 19, 3, 21, 8]

root = build_tree(preorder, inorder)

print("In-order traversal of the constructed tree:")
print_inorder(root)

print("\nVisualizing the constructed tree:")
visualize_tree(root)
