import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json

def main():

	G = openGraph()
	labels = {}
	print G.nodes()
	print G.edges()
	pos = nx.spring_layout(G) # positions for all nodes

	color=nx.get_node_attributes(G,'group')
	print color	
	print color['1']

	for i in range(1,len(G)+1):
		labels[str(i)] = str(i)

	nx.draw_networkx_labels(G,pos,labels)

	node_list_red = ['1','2','3']
	node_list_blue = ['4','5','6','7']
	nx.draw_networkx_nodes(G,pos, nodelist=node_list_red, node_color='r')
	nx.draw_networkx_nodes(G,pos,nodelist=node_list_blue, node_color='b')
	nx.draw_networkx_edges(G,pos)
	#nx.draw(G, with_labels = True)
	plt.axis('off')
#	plt.savefig("labels_and_colors.png") 
	plt.show()


def openGraph():

	with open('graph1.json') as f:
        	js_graph = json.load(f)
###	print len(js_graph['nodes'])
	return json_graph.node_link_graph(js_graph, False, {'color':'black','visited':'false'})



	
	 

if __name__ == "__main__":
    main()
