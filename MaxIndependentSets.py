import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json


def main():

	G = openGraph()
	nodes = G.nodes()
	edges = G.edges()
	print ""
	FindMaxIndependentSet(G,'1')
	
	coloredGraph = ColorGraph(G)
	labels = coloredGraph[0]

	pos = nx.spring_layout(G) # positions for all nodes
	nx.draw_networkx_labels(G,pos,labels)
	nx.draw_networkx_nodes(G,pos,nodelist=coloredGraph[1], node_color='r')
	nx.draw_networkx_nodes(G,pos,nodelist=coloredGraph[2], node_color='b')
	nx.draw_networkx_nodes(G,pos,nodelist=coloredGraph[3], node_color='y')
	nx.draw_networkx_nodes(G,pos,nodelist=coloredGraph[4], node_color='g')
	nx.draw_networkx_nodes(G,pos,nodelist=coloredGraph[5], node_color='purple')
	nx.draw_networkx_edges(G,pos)
	
	plt.axis('off')
	plt.show()


def ColorGraph(G):

	node_list_red = []
	node_list_blue = []
	node_list_yellow = []
	node_list_green = []
	node_list_purple = []	

	labels = {}
	
	color=nx.get_node_attributes(G,'color')
	
#	red = len(node_list_red)
#	blue = len(node_list_blue)
#	yellow = len(node_list_yellow)
#	green = len(node_list_green)	
#	maxColor = "red"

	for i in range(1,len(G)+1):
		labels[str(i)] = str(i)
		
		if(color[str(i)] == 1):
			node_list_red.append(str(i))	
#			red = len(node_list_red)
		elif(color[str(i)] == 2):
			node_list_blue.append(str(i))
#			blue = len(node_list_blue)		
		elif(color[str(i)] == 3):
			node_list_yellow.append(str(i))
#			yellow = len(node_list_yellow)
		elif(color[str(i)] == 4):
			node_list_green.append(str(i))		
#			green = len(node_list_green)
		elif(color[str(i)] == 5):
			node_list_purple.append(str(i))
#		newMax = max(red,blue,yellow,green)
#		if(maxColor != newMax):
#			maxColor = newMax

	if len(node_list_blue) > len(node_list_red):
		print len(node_list_blue),
		print len(node_list_red),
	else:
		print len(node_list_red),
		print len(node_list_blue),

	if len(node_list_yellow) != 0: print len(node_list_yellow),
	if len(node_list_green) != 0: print len(node_list_green),
	if len(node_list_purple) != 0: print len(node_list_purple)

	print ""

	print "RED: ",
	print node_list_red
	print "BLUE: ",
	print node_list_blue
	print "YELLOW: ",
	print node_list_yellow
	print "GREEN: ",
	print node_list_green
	print "PURPLE: ",
	print node_list_purple
	
	return labels, node_list_red, node_list_blue, node_list_yellow, node_list_green, node_list_purple
	
	
def openGraph():
	with open("graph7.json") as f:
        	js_graph = json.load(f)
	return json_graph.node_link_graph(js_graph, False)

def FindMaxIndependentSet(G,v):
	next = []
	nodes = G.nodes()
	adjColors = []
	current = nodes[v]
	current['visited'] = 1
	neighbors = G.neighbors(v)
	for n in neighbors:
		if nodes[n]['visited'] == 1:
			adjColors.append(nodes[n]['color'])	
		else:	
			next.append(n)	
	if(1 not in adjColors):
		print "Keeping " + v + " as RED."
	elif(2 not in adjColors):
		print "Changing " + v + " to BLUE."
		nodes[v]['color'] = 2
	elif(3 not in adjColors):
		print "Changing " + v + " to YELLOW."
		nodes[v]['color'] = 3
	elif(4 not in adjColors):
		print "Changing " + v + " to GREEN."
		nodes[v]['color'] = 4
	elif(5 not in adjColors):
		print "Changing " + v + " to PURPLE."
		nodes[v]['color'] = 5
		
	
	for n in next:
		if nodes[n]['visited'] == 0:
			FindMaxIndependentSet(G,n) 

if __name__ == "__main__":
    main()
