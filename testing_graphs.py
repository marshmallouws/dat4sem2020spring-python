import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import re
from flask import Flask, render_template_string, Markup

# https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat
airports = set() # nodes
dep = []

# Each line contains two airports, from and to. Find these using regex.
# Airports are defined in IATA-format and are immediatly followed by a , (use lookaheads)

# Use regex to find the from and to airport. Use this to make a list of
# all airports and a list of a set of airports --> Used for edges

# Create a directed graph and find the 30 airports with most edges (both
# in and out) 

# Draw a graph over this subgraph.

"""
 Airports are written by using AITA (Three uppercase letters eg. CPH) 
 and are immediatly followed by a , (Only looking for three uppercase letters returns
 cases that are not airports). Make a list of distinct airports.
"""

"""
Create a directed graph and find the 30 airports with the most edges.
Draw a graph over this subgraph
"""

"""
Create a flask server that can show this graph
"""



# Iterate through data to find airport codes (2. and 4. index)
with open('routes.dat.txt', 'r') as f:
    fr = re.compile(r'[A-Z]{3}(?=,)')
    for line in f:
        air = fr.findall(str(line))
        airports.add(air[0])
        airports.add(air[1])
        dep.append((air[0], air[1]))

def create_graph():
    graph = nx.DiGraph()
    graph.clear()

    for idx, name_pair in enumerate(airports):
        graph.add_node(idx, name=' '.join(name_pair))
    
    # graph.add_nodes_from(all_names_list)
    graph.add_edges_from(dep)

    return graph

def draw_graph(graph):
    nx.draw(graph, pos=graphviz_layout(graph), 
            node_size=30, width=.05, cmap=plt.cm.Blues, 
            with_labels=True, node_color=range(len(graph)))


# Find the 30 airports with most edges (both in and out)
graph = create_graph()

a = dict(graph.degree()).items()
b = sorted(a, key = lambda x : x[1])
print([n for n, e in b[-30:]])

# Draw a graph over these
ca = graph.subgraph([x[0] for x in b[-30:]])
plt.show(block = False)
draw_graph(ca)
plt.savefig('Graph.svg', format='SVG')


print(max(dict(graph.degree()).items(), key= lambda x: x[1]))


n = nx.shortest_path(ca)
print('Something: ', n)

# Create a flask server and plot the graph on this. Additional: Make a calculator on the app
# That calculates the shortest path between two points
app = Flask(__name__)

tmpl = """{% block content %}
<section>
    {{ svg }}
</section>
{% endblock %}"""

@app.route('/')
def show_svg():
    svg = open('Graph.svg').read
    return render_template_string(tmpl, svg=Markup(svg()))
