import networkx as nx
import matplotlib


def tutorial():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_nodes_from([
        (4, {"color": "red"}),
        (5, {"color": "green"}),
    ])
    H = nx.path_graph(10)
    G.add_nodes_from(H)
    nx.draw(G)

    G.add_edge(1, 2)
    e = (2, 3)
    G.add_edge(*e)  # unpack edge tuple*
    nx.draw(G)

    G.add_edges_from([(1, 2), (1, 3)])
    G.add_edges_from(H.edges)
    G.clear()
    nx.draw(G)
    nx.draw(H)

    G.add_edges_from([(1, 2), (1, 3)])
    G.add_node(1)
    G.add_edge(1, 2)
    G.add_node("spam")  # adds node "spam"
    G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
    G.add_edge(3, 'm')
    nx.draw(G)
    print(G.number_of_nodes())

    DG = nx.DiGraph()
    DG.add_edge(2, 1)  # adds the nodes in order 2, 1
    DG.add_edge(1, 3)
    DG.add_edge(2, 4)
    DG.add_edge(1, 2)
    assert list(DG.successors(2)) == [1, 4]
    assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)]

    nx.draw(DG)
    print(G.nodes)
    print(G.edges)
    print(G.adj[1])

    print(G.degree[1])  # the number of edges incident to 1

    G.remove_node(2)
    G.remove_nodes_from("spam")
    print(G.nodes)

    G.add_edge(1, 2)
    H = nx.DiGraph(G)  # create a DiGraph using the connections from G
    print(H.edges())
    edgelist = [(0, 1), (1, 2), (2, 3)]
    H = nx.Graph(edgelist)

    G = nx.Graph([(1, 2, {"color": "yellow"})])
    print(G[1])  # same as G.adj[1]
    print(G[1][2])
    print(G.edges[1, 2])

    G.add_edge(1, 3)
    G[1][3]['color'] = "blue"
    G.edges[1, 2]['color'] = "red"
    print(G.edges[1, 2])
    print(G)
    print(G.nodes)
    print(G.edges)

    FG = nx.Graph()
    FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
    for n, nbrs in FG.adj.items():
        for nbr, eattr in nbrs.items():
            wt = eattr['weight']
            if wt < 0.5: print(f"({n}, {nbr}, {wt:.3})")

    print("Кромки")
    for (u, v, wt) in FG.edges.data('weight'):
        if wt < 0.5:
            print(f"({u}, {v}, {wt:.3})")

    G = nx.Graph(day="Friday")
    print(G.graph)
    G.graph['day'] = "Monday"
    print(G.graph)

    G.add_node(1, time='5pm')
    G.add_nodes_from([3], time='2pm')
    print(G.nodes[1])
    G.nodes[1]['room'] = 714
    print(G.nodes.data())

    G.add_edge(1, 2, weight=4.7)
    G.add_edges_from([(3, 4), (4, 5)], color='red')
    G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
    G[1][2]['weight'] = 4.7
    G.edges[3, 4]['weight'] = 4.2
    print(G)
    print(G.nodes.data())

    #  Directed graphs¶
    DG = nx.DiGraph()
    DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
    print(DG.out_degree(1, weight='weight'))

    print(DG)
    print(DG.nodes.data())

    DG.degree(1, weight='weight')
    print(DG.successors(1))
    print(DG.neighbors(1))
    print(DG)
    print(DG.nodes.data())

    H = nx.Graph(G)  # create an undirected graph H from a directed graph G
    print(H)
    print(H.nodes.data())

    #  Multigraphs
    MG = nx.MultiGraph()
    MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
    dict(MG.degree(weight='weight'))
    GG = nx.Graph()
    for n, nbrs in MG.adjacency():
        for nbr, edict in nbrs.items():
            minvalue = min([d['weight'] for d in edict.values()])
            GG.add_edge(n, nbr, weight=minvalue)

    print(nx.shortest_path(GG, 1, 3))

    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3)])
    G.add_node("spam")  # adds node "spam"
    list(nx.connected_components(G))

    print(sorted(d for n, d in G.degree()))
    print(nx.clustering(G))

    sp = dict(nx.all_pairs_shortest_path(G))
    print(sp[3])

    G = nx.petersen_graph()
    subax1 = matplotlib.pyplot.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    subax2 = matplotlib.pyplot.subplot(122)
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    matplotlib.pyplot.show()

    options = {
        'node_color': 'black',
        'node_size': 100,
        'width': 3,
    }
    subax1 = matplotlib.pyplot.subplot(221)
    nx.draw_random(G, **options)
    subax2 = matplotlib.pyplot.subplot(222)
    nx.draw_circular(G, **options)
    subax3 = matplotlib.pyplot.subplot(223)
    nx.draw_spectral(G, **options)
    subax4 = matplotlib.pyplot.subplot(224)
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], **options)
    G = nx.dodecahedral_graph()
    shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
    nx.draw_shell(G, nlist=shells, **options)
    nx.draw(G)
    matplotlib.pyplot.savefig("path.png")

    # from networkx.drawing.nx_pydot import write_dot
    # pos = nx.nx_agraph.graphviz_layout(G)
    # nx.draw(G, pos=pos)
    # write_dot(G, 'file.dot')

    G = nx.complete_graph(5)
    nx.draw(G)

    #  G = nx.complete_graph(5)
    #  A = nx.nx_agraph.to_agraph(G)
    #  H = nx.nx_agraph.from_agraph(A)

    # Introduction to NetworkX in Python
    G = nx.barabasi_albert_graph(100,2)
    nx.draw_spring(G)


