from graphviz import Digraph

NAME = "familytree"
ENGINE = "dot"
TABCHAR = "    "
FORMATS = ["png", "pdf", "bmp"]
NODE_ATTRS = {
    "shape": "rectangle",
    "style": "rounded"
}
GRAPH_ATTRS = {
    "rankdir": "LR"
}


dot = Digraph(name=NAME,
              engine=ENGINE, 
              node_attr=NODE_ATTRS, 
              graph_attr=GRAPH_ATTRS)

def recurse_tree(parent, depth, source):
    try:
        last_line = next(source)
    except:
        return

    while last_line:
        tabs = last_line.count(TABCHAR)
        if tabs < depth:
            break
        node = last_line.strip()
        if tabs >= depth:
            if parent is not None:
                dot.edge(parent, node)
            last_line = recurse_tree(node, tabs+1, source)
    return last_line

buff = []
with open(NAME+".txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.rstrip()
        if line.strip() == "":
            continue
        else:
            buff.append(line.replace(line.strip(), str(i))+"\n")
        dot.node(str(i), line.strip())

recurse_tree(None, 0, (i for i in buff))

for fmt in FORMATS:
    dot.render(view=False, cleanup=True, format=fmt, filename="output/"+NAME)