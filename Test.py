#!/usr/bin/python3
#author:Hamid.19-07-2017
from  Graph import Graph
#Test methods
def test1():
    graph = Graph.graphreader("graph1.txt")
    src = graph.get_node_by_label(1)
    d = graph.linkState(src)
    for element in sorted(d):
        print("Path from " + str(src) + " to Node " +str(element) +
              " : Length :" + str(d[element][0]) + ". Preceding : " + str(d[element][1]) )
    for element in sorted(d):
        cost,pred = d[element]
        print("From Node:" + "Cost")
        print(element,'       :',cost, '(', pred ,')')
def test2():
    graph = Graph.graphreader("simplegraph2.txt")
    src = graph.get_node_by_label(14)
     
    d = graph.linkState(src)
    for element in d:
        print("Path from "+str(src) + "  to Node " + str(element)
            + ". Length :" + str(d[element][0]) + ". Preceding : " + str(d[element][1]))
        for element in sorted(d):
            cost,pred = d[element]
            print("From Node:" + "Cost")
            print(element,'       :',cost, '(', pred ,')')

if __name__=="__main__":
    test1()
    test2()
