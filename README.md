# Featured Graph Informatics

Calculations of graph informatics (mainly entropy) for graphs with features to evaluate the results of graph reduction

Input:
A DataFrame of node table in the following format

    |   node_id   |   feature_1   |   feature_2   |   ...   |   feature_m   |
    |:---:|:---:|:---:|:---:|:---:|
    | NODEID_1 | x1_1 | x1_2 | ... | x1_m |
    | NODEID_2 | x2_1 | x2_2 | ... | x2_m |
    | ... | ... | ... | ... | ... | ... |
    | NODEID_n | xn_1 | xn_2 | ... | xn_m |
    
A DataFrame of edge table in the following format

    |   node1_id   |   node2_id   |   feature_1   |   feature_2   |   ...   |   feature_i   |
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | NODEID_1 | NODEID_2 | x1_12 | x2_12 | ... | xi_12 |
    | NODEID_1 | NODEID_3 | x1_13 | x2_13 | ... | xi_13 |
    | ... | ... | ... | ... | ... | ... |
    | NODEID_n | NODEID_k | x1_nk | x2_nk | ... | xi_nk |
