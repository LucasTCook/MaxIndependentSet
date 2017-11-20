import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json

def main():

	G = openGraph()

	labels = {}
	node_list_red = []
	node_list_blue = []
	node_list_green = []
	node_list_yellow = []
	nodes = G.nodes()
	edges = G.edges()
	pos = nx.spring_layout(G) # positions for all nodes

	print "Neighbor of '1':",
	neighbors = G.neighbors('1')
	for n in neighbors:
		print n,


	#
	# Must call nodes in the array associatively 
	# 

	print "Node[0]: ",
	print nodes['1']['color'],

	FindMaxIndependentSet(G,nodes['1'])
	color=nx.get_node_attributes(G,'color')

	print G
	
	for i in range(1,len(G)+1):
		labels[str(i)] = str(i)
		
		if(color[str(i)] == 1):
			node_list_red.append(str(i))	
		if(color[str(i)] == 2):
			node_list_blue.append(str(i))		
		if(color[str(i)] == 3):
			node_list_green.append(str(i))		
		if(color[str(i)] == 4):
			node_list_yellow.append(str(i))		
	nx.draw_networkx_labels(G,pos,labels)

	nx.draw_networkx_nodes(G,pos,nodelist=node_list_red, node_color='r')
	nx.draw_networkx_nodes(G,pos,nodelist=node_list_blue, node_color='b')
	nx.draw_networkx_nodes(G,pos,nodelist=node_list_green, node_color='g')
	nx.draw_networkx_nodes(G,pos,nodelist=node_list_yellow, node_color='y')
	nx.draw_networkx_edges(G,pos)
	#nx.draw(G, with_labels = True)
	plt.axis('off')
#	plt.savefig("labels_and_colors.png") 
	plt.show()


def openGraph():

	with open('graph1.json') as f:
        	js_graph = json.load(f)
	return json_graph.node_link_graph(js_graph, False)

def FindMaxIndependentSet(G,v):
	v['visited'] = 1
	v['color'] = 3


	
	 

if __name__ == "__main__":
    main()
