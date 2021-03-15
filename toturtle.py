import rdflib


g = rdflib.Graph()

res = g.parse("documentprojet.rdf",format="xml")

s = (g.serialize(format="turtle").decode("utf-8"))


f = open("reponseTurtle", "w")
f.write(s)
f.close()