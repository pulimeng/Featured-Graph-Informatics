# Featured Graph Informatics

Calculations of graph informatics (mainly entropy) for graphs with features to evaluate the results of graph reduction

# Dependencies

1. pandas
2. networkx
3. numpy
4. scipy   

# Usage

Inputs:

A DataFrame of node table in the following format:

|   node_id   |   feature_1   |   feature_2   |   ...   |   feature_m   |
|:---:|:---:|:---:|:---:|:---:|
| NODEID_1 | x1_1 | x1_2 | ... | x1_m |
| NODEID_2 | x2_1 | x2_2 | ... | x2_m |
| ... | ... | ... | ... | ... | ... |
| NODEID_n | xn_1 | xn_2 | ... | xn_m |
    
A DataFrame of edge table in the following format:

|   node1_id   |   node2_id   |   feature_1   |   feature_2   |   ...   |   feature_i   |
|:---:|:---:|:---:|:---:|:---:|:---:|
| NODEID_1 | NODEID_2 | x1_12 | x2_12 | ... | xi_12 |
| NODEID_1 | NODEID_3 | x1_13 | x2_13 | ... | xi_13 |
| ... | ... | ... | ... | ... | ... |
| NODEID_n | NODEID_k | x1_nk | x2_nk | ... | xi_nk |

Example of node table and edge table is provided in this repo, namely, `reduced_nodes.csv` and `reduced_edges.csv`.
To run the code, run `python featured_graph_entropy.py --nfile node_file --efile edge_file --node node_column_name --edge edge_column_name1,edge_column_name2`.
To use the example files, run `python featured_graph_entropy.py --nfile ./reduced_nodes.csv --efile ./reduced_edges.csv --node ensembl --edge protein1,protein2`.
