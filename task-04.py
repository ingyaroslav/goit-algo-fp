import uuid
import networkx as nx

import matplotlib
matplotlib.use('GTK3Agg')  # Використання бекенда GTK3Agg

import matplotlib.pyplot as plt

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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def draw_heap(heap):
    heap_tree = nx.DiGraph()
    pos = {}

    for i, val in enumerate(heap):
        node = Node(val)
        node.id = str(uuid.uuid4())
        heap_tree.add_node(node.id, label=str(val))

        if i == 0:
            pos[node.id] = (0, -1)
        elif i % 2 == 0:  # right child
            pos[node.id] = (pos[heap_tree.nodes()[i // 2]][0] + 1, -1)
        else:  # left child
            pos[node.id] = (pos[heap_tree.nodes()[i // 2]][0] - 1, -1)

        parent_id = heap_tree.nodes()[i // 2] if i // 2 < len(heap_tree.nodes()) else None
        if parent_id:
            heap_tree.add_edge(parent_id, node.id)


    colors = ["skyblue"] * len(heap)  # Задаємо всім вузлам колір
    labels = {node[0]: node[1]['label'] for node in heap_tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад використання
heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
draw_heap(heap)
