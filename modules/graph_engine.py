from typing import List
import modules.database_handler as database_handler

file_path = 'C:\Users\Bladimir Kolodzie\Desktop\00\notebooks\Hub_Notebook\Summer 2026\11 Projects\00_Project_CS\x\database\etfs.json'
class Node(object):

  def __init__(self, name):
 
    self._name = name

  def get_name(self, name):
    return self._name

  def __str__(self):
    return self._name

class Edge(Node):
  '''
  Edge e connect direct graphs a1 and a2 trough edges e1 . . . e2, a1 => a2
  src: source(node)
  dst: destination(ode)
  '''
  def __init__(self, src, dst, edge_name):
    self._src = src
    self._dst = dst
    self._edge_name = edge_name
# get source node
  def get_source(self):
    return self._src
# get destination node
  def get_destination(self):
    return self._dst

  def get_edge_name(self):
    return self._edge_name


# i left this one here to compare the use of clas_var + str + class_var, vs f_string literal
  def relation(self):
    print(f" relation type:{self._edge_name} a1: {self._src} => a2:{self._dst}")

  def __str__(self):
    # source and destination are Node type objects so use the get_name() method is possible
    self._src.get_name() + '->' + self._dst.get_name()



class Weighted_edge(Edge):
  def __init__(self, src, dst, weight= 1.0):
    self._src = src
    self._dst = dst
    self._weight = weight

  def get_weight(self):
    return self._weight

  def __str__(self):
    return(f'{self._src.get_name()} => ({self._weight})' + f'{self._dst.get_name()}')










class Diagraph(object):
  '''
  node: str literal of the node name
  data: in the furue json files, for now i will acess them dynamically in the ram the json will be for data storing

  the variable edges is a dictionary mapping node name to a list of connections of such node
  '''
  def __init__(self, nodes: List, Edges: dict, data):
    self._nodes = []
    # data will be a database of json files maybe using mongodb
    self._data = {}
    # A dictionary that contain connections between edges
    self._edges = {}


  def add_node(self, node):
    if node in self._nodes:
      raise ValueError('Duplicate node')
    else:
      # Add node to nodes list
      self._nodes.append(node)
      # Create a key in _edges dict and assign an empty list as the value
      self._edges[node] = []

  def add_edge(self, edge):
    '''
    input edge
    '''
    src = edge.get_source()
    dest = edge.get_destination()

    if not(src in self._nodes and dest in self._nodes):
      raise ValueError('Node not in graph')
    # Acess to the key node and add to its list the destination
    self._edges[src].append(dest)


# Interface
  def get_node(self):
    return self._node

  def childrens_of(self, node):
    # acess dictionary values using a key
    return self.edges[node]

  def has_node(self, node):
    return node in self._nodes
  
  
  def save_json(self):
    x = database_handler(file_path)
    x.write_data()

  def __str__(self):
    result = ''
    for source in self._nodes:
        for destination in self._edges[source]:
          result = (result + source.get_name() + '->' + destination.get_name() + '\n') # we can use get_name method cuz source is an node type object
    return result[:-1] #omit final newline

class Graph(Diagraph):
  def add_edge(self, edge):
    Diagraph.add_edge(self, edge) # call itself
    rev = Edge(edge.get_destination(), edge.get_source())
    Diagraph.add_edge(self, rev)
