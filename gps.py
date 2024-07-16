import xml.etree.ElementTree as et
# https://chatgpt.com/c/ffc22df0-cd1f-40a5-8064-f76c6428f945

from data import way
from data import tag
from data import node
from data import member
from data import relation
from add import add_parallel_points


def load_xml_values(path):
    xml = et.iterparse(path)
    nodes = []
    ways = []
    nds = []
    tags = []
    todos_postes = []

    for event, elem in xml:
        if event == 'end':
            type = elem.tag

            if type == 'tag':
                tags.append(tag.Tag(elem.attrib['k'],elem.attrib['v']))

            if type == 'nd':
                nds.append(elem.attrib['ref'])

            if type == 'node':
                nodes.append(node.Node(elem.attrib['id'],elem.attrib['lat'],elem.attrib['lon'],tags.copy()))
                tags.clear()

            if type == 'way':
                if any(t.name == 'highway' for t in tags):
                    node_values = []
                    gps = []
                    for n in nodes:
                        if any(nd == n.id for nd in nds):
                            node_values.append(n)
                            gps.append((float(n.lat),float(n.lon)))

                    postes = add_parallel_points(gps,10,10)
                    todos_postes += postes

                    ways.append(way.Way(elem.attrib['id'],node_values.copy(),postes.copy(),tags.copy()))
                
                nds.clear()
                tags.clear()

    # for n in nodes:
    #     print(f"Node:{n.id},LT:{n.lat},LN:{n.lon},Tags:{len(n.tags)}")

    # for w in ways:
    #     print(f"Way:{w.id},NDs:{len(w.nds)},Tags:{len(w.tags)}")

    with open("postes.csv","x") as f:
        for p in todos_postes:
            f.write(f"\"{p[0]}\";\"{p[1]}\"\n")



#   <tag k="highway" v="residential"/>




if __name__ == '__main__':
    load_xml_values('./map (1).osm')