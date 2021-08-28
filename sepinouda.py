# Introduction to Data Science - NetworkX Tutorial by Sepinoud Azimi

import networkx as nx

def sepinouda():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    G = nx.Graph()
    G.add_edge('A', 'B', weight=13, relation='friend')
    G.add_edge('B', 'C', weight=9, relation='family')
    G.add_edge('B', 'D', weight=7, relation='friend')
    G.add_edge('E', 'B', weight=10, relation='friend')
    G.add_edge('E', 'A', weight=1, relation='enemy')
    G.add_edge('F', 'B', weight=13, relation='family')
    G.edges(data=True)
