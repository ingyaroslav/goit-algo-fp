import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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

def depth_first_traversal(node, visited, colors, color=(0.2, 0.8, 0.2)):
    if node is None:
        return
    
    visited.add(node)
    colors[node.id] = color
    
    for child in [node.left, node.right]:
        if child is not None and child not in visited:
            depth_first_traversal(child, visited, colors, tuple(c * 0.9 for c in color))

def breadth_first_traversal(root, colors):
    if root is None:
        return
    
    visited = set()
    queue = deque([root])
    color = (0.2, 0.2, 0.8)
    
    while queue:
        node = queue.popleft()
        visited.add(node)
        colors[node.id] = color
        
        for child in [node.left, node.right]:
            if child is not None and child not in visited:
                queue.append(child)
                visited.add(child)
                colors[child.id] = tuple(c * 0.9 for c in color)

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    plt.figure(figsize=(8, 5))

    # Обхід в глибину
    dfs_colors = {}
    depth_first_traversal(tree_root, set(), dfs_colors)
    nx.draw(tree, pos=pos, labels={node[0]: node[1]['label'] for node in tree.nodes(data=True)}, arrows=False, node_size=2500, node_color=list(dfs_colors.values()))

    plt.title("DFS (Depth-First Search) Traversal")
    plt.show()

    plt.figure(figsize=(8, 5))

    # Обхід в ширину
    bfs_colors = {}
    breadth_first_traversal(tree_root, bfs_colors)
    nx.draw(tree, pos=pos, labels={node[0]: node[1]['label'] for node in tree.nodes(data=True)}, arrows=False, node_size=2500, node_color=list(bfs_colors.values()))

    plt.title("BFS (Breadth-First Search) Traversal")
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)
