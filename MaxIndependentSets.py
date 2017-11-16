import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json

def main():

	G = openGraph()
	plt.show()
	FindMaxIndependentSet()


def openGraph():

	with open('graph1.json') as f:
        	js_graph = json.load(f)

	return json_graph.node_link_graph(js_graph)

def FindMaxIndependentSet(graph, vertex):
      label v as discovered
      for all edges from v to w in G.adjacentEdges(v) do
          if vertex w is not labeled as discovered then
              recursively call DFS(G,w)


class Graph():
	Vertices = []
	Edges = [][]	
	
	
	def findEdges():
		//
		//
		//
	
	 
class Colors():

if __name__ == "__main__":
    main()
