# Introduction to Data Science - NetworkX Tutorial by Sepinoud Azimi
import matplotlib
import networkx as nx
#  import matplotlib.pyplot as plt

def main():
    g: Graph = nx.Graph()
    g.add_edge('A', 'B', weight=13, relation='friend')
    g.add_edge('B', 'C', weight=9, relation='family')
    g.add_edge('B', 'D', weight=7, relation='friend')
    g.add_edge('E', 'B', weight=10, relation='friend')
    g.add_edge('E', 'A', weight=1, relation='enemy')
    g.add_edge('F', 'B', weight=13, relation='family')
    g.edges(data=True)

    g.add_node('A', role='Trader')
    g.add_node('B', role='Analyst')
    g.add_node('C', role='Manager')
    g.nodes(data=True)

    print(g)
    print(g.nodes.data())

    nx.draw(g)
    nx.draw_networkx(g, with_labels=True)

    from networkx.algorithms import bipartite
    B = nx.Graph()
    B.add_nodes_from(['A','B','C','D','E'],bipartite=0)
    B.add_nodes_from([1,2,3,4],bipartite=1)
    B.add_edges_from([('A',1),('B',1),('C',1),('C',3),('D',4),('E',1),('A',2),('E',2)])
    bipartite.is_bipartite(B)

    edges = B.edges()
    nx.draw_networkx(
        B,
        pos=nx.drawing.layout.bipartite_layout(B, ['A', 'B', 'C', 'D', 'E']),
        width=2)
    print(edges)
