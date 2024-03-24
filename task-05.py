import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def depth_first_traversal(node, depth=0):
    if node is not None:
        color = "#{:02X}{:02X}{:02X}".format(255 - depth * 10, 128, 255 - depth * 10)  # Створення колірного коду RGB
        node.color = color
        print(node.val)  # Виведення значення вузла
        depth_first_traversal(node.left, depth + 1)
        depth_first_traversal(node.right, depth + 1)

def breadth_first_traversal(root):
    queue = [root]
    depth = 0
    while queue:
        next_level = []
        for node in queue:
            color = "#{:02X}{:02X}{:02X}".format(255 - depth * 10, 128, 255 - depth * 10)  # Створення колірного коду RGB
            node.color = color
            print(node.val)  # Виведення значення вузла
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level
        depth += 1

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід дерева у глибину та відображення
depth_first_traversal(root)
draw_tree(root)

# Обхід дерева в ширину та відображення
breadth_first_traversal(root)
draw_tree(root)
