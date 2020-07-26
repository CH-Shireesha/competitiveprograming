class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)


    def get_edge_list(self):
        edge_list = []
        for edge in self.edges:
            edge_list.append((edge.value,edge.node_from.value,edge.node_to.value))
        return edge_list


    def get_adjacency_list(self):
        max_index = len(self.nodes)
        adjacency_list = [None] * (max_index + 1)
        for node in self.nodes:
            sub_list = []
            for edge in self.edges:
                sub_list.append((edge.node_from.value,edge.value))
            adjacency_list[node.value] = sub_list
        print(adjacency_list)
        return adjacency_list
    
    
    def get_adjacency_matrix(self):
        max_index = len(self.nodes)
        adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
        for node in self.nodes:
            for edge in self.edges:
                adjacency_matrix[node.value][edge.node_from.value] = edge.value
        return adjacency_matrix

