# Introduction to Data Science - NetworkX Tutorial by Sepinoud Azimi

import networkx as nx


def main():
    g = nx.Graph()
    g.add_edge('A', 'B', weight=13, relation='friend')
    g.add_edge('B', 'C', weight=9, relation='family')
    g.add_edge('B', 'D', weight=7, relation='friend')
    g.add_edge('E', 'B', weight=10, relation='friend')
    g.add_edge('E', 'A', weight=1, relation='enemy')
    g.add_edge('F', 'B', weight=13, relation='family')
    g.edges(data=True)

    g.add_node('A',role='Trader')
    g.add_node('B',role='Analyst')
    g.add_node('C',role='Manager')
    g.nodes(data=True)

    nx.draw(g)
