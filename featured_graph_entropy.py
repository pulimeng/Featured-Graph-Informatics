import argparse

import pandas as pd
import networkx as nx

import numpy as np
from scipy.stats import entropy
from scipy.sparse import csr_matrix, csgraph

def iso_check(node_table, edge_table, node_col_name, edge_col_names):
    """
    check if there is isolated nodes
    Inputs:
    node_table -- node table in the format of dataframe
    edge_table -- edge table in the format of dataframe
    node_col_name -- string, name of the column that contains node id in the node table
    edge_col_names -- list, names of the columns that contains node ids for edges in the edge table
    Outputs:
    None
    """
    num_nodes = len(node_table[node_col_name].unique().tolist())
    num_nodes_from_edge = len(set(edge_table[edge_col_names[0]].unique().tolist() + edge_table[edge_col_names[1]].unique().tolist()))
    if num_nodes > num_nodes_from_edge:
        print('Isolated nodes found in reduced graph')
    elif num_nodes == num_nodes_from_edge:
        print('No isolated nodes in reduced graph')
    else:
        print('Error in the reduced graph')
    
def graph_construction(node_table, edge_table, node_col_name, edge_col_names):
    """
    Construct graphs and feature matrix
    Inputs:
    node_table -- node table in the format of dataframe
    edge_table -- edge table in the format of dataframe
    node_col_name -- string, name of the column that contains node id in the node table
    edge_col_names -- list, names of the columns that contains node ids for edges in the edge table
    Outputs:
    X -- feature matrix (num_nodes x num_features)
    A -- adjacency matrix (num_nodes x num_nodes
    """
    G = nx.from_pandas_edgelist(edge_table, source=edge_col_names[0], target=edge_col_names[1])
    # the following steps are very important since it ensures the order of nodes in the node table is the same as the order
    # or nodes from graph constructed by networkx
    nx_node_list = list(G.nodes)
    node_table = node_table.set_index(node_col_name)
    node_table = node_table.reindex(nx_node_list)
    node_table = node_table.reset_index()
    X = node_table.iloc[:, [1,2,4]].to_numpy() # this selects the column(s) of the features you want to use
    A = nx.to_numpy_array(G, nodelist=nx_node_list)
    return X, A

"""
Calculate the feature only Shannon's entropy and the featured-graph Shannon's entropy
"""
def feature_entropy(X):
    """
    Shannon's entropy for features only normalized by the total amount information
    Inputs:`
    X -- feature matrix
    Outputs:
    H -- Shannon's entropy for features only
    """
    H = 0
    for i in range(X.shape[1]):
        _, cnts = np.unique(X[:,i], return_counts=True)
        I0 = np.log2(X.shape[0])
        H +=  entropy(cnts, base=2)/I0
    return H/X.shape[1]

def fgraph_entropy(X, A):
    """
    Featured-graph entropy normalized by the total amount information
    Inputs:
    X -- feature matrix
    A -- adjacency matrix
    Outputs:
    H -- featured-graph entropy
    """
    H = 0
    X = csr_matrix(X)
    A = csr_matrix(A)
    L = csgraph.laplacian(A, normed=True)
    h = L * X
    for i in range(3):
        target = h.toarray()[:,i]
        _, cnts = np.unique(target, return_counts=True)
        I0 = np.log2(X.shape[0])
        H += entropy(cnts, base=2)/I0
    return H/X.shape[1]

def main(opt):
    nodes = pd.read_csv(opt.nfile)
    edges = pd.read_csv(opt.efile)
    edge_names = opt.edge.split(',')
    iso_check(nodes, edges, node_col_name=opt.node, edge_col_names=[edge_names[0], edge_names[1]])
    X, A = graph_construction(nodes, edges, node_col_name=opt.node, edge_col_names=[edge_names[0], edge_names[1]])
    return feature_entropy(X), fgraph_entropy(X, A)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--nfile', type=str, help='Node table file name')
    parser.add_argument('--efile', type=str, help='Edge table file name')
    parser.add_argument('--node', type=str, help='Node column name')
    parser.add_argument('--edge', type=str, help='Edge column names')
    opt = parser.parse_args()
    H0, H = main(opt)
    print('Feature only entropy after reduction: {:.4f}'.format(H0))
    print('Featured-graph entropy after reduction: {:.4f}'.format(H))