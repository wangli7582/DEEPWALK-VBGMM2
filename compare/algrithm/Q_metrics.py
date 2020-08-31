def cal_Q(partition, G):
    m = len(G.edges(None, False))
    a = []
    e = []

    for community in partition:
        t = 0.0
        for node in community:
            t += len(list(G.neighbors(node)))
        a.append(t / (2 * m))

    for community in partition:
        t = 0.0
        for i in range(len(community)):
            for j in range(len(community)):
                if (G.has_edge(community[i], community[j])):
                    t += 1.0
        e.append(t / (2 * m))

    q = 0.0
    for ei, ai in zip(e, a):
        q += (ei - ai ** 2)

    return q

if __name__ == '__main__':
    dataset_path = '../network/club.txt'
    G4 = nx.read_edgelist('../network/club.txt')
    array = np.array(nx.to_numpy_matrix(G4))
    cluster = GN.gn(dataset_path)
    print(Q(array, cluster))

