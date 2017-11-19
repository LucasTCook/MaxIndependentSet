import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json

def main():

	G = openGraph()
	print G.nodes()
	print G.edges()
	pos=nx.spring_layout(G) # positions for all nodes
	node_list_red = ['1','2','3']
	node_list_blue = ['4','5','6','7']
	nx.draw_networkx_nodes(G,pos,nodelist=node_list_red, node_color='r')
	nx.draw_networkx_nodes(G,pos,nodelist=node_list_blue, node_color='b')
	nx.draw_networkx_edges(G,pos)
	#nx.draw(G, with_labels = True)
	plt.show()


def openGraph():

	with open('graph1.json') as f:
        	js_graph = json.load(f)
	print len(js_graph['nodes'])
	return json_graph.node_link_graph(js_graph, False, dict(color='black',visited='false'))



	
	 

if __name__ == "__main__":
    main()
