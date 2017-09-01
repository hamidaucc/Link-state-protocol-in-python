#!/usr/bin/python3
#author:Hamid.19-07-2017
from node import Node
from link import Link
from apq_heap import APQHeap
'''
This project implenments the OSPF using Dijkstra algorithm (Open Shortest Path First) network protocol in python.

 Link-State Routing protocol is a main class of routing protocols.
 It is performed by every switching node/router in the network.
 The basic concept of link-state routing is that every node
 constructs a map of the connectivity to the network, in the
 form of a Graph, showing which nodes are connected to which
 other nodes. Each node then independently calculates the next
 best logical path from it to every possible destination in the network.
 The collection of best paths will then form the node's routing table.
OSPF:
-----
Open Shortest Path First (OSPF) is a link-state routing protocol for Internet 
Protocol (IP) networks. It uses a link state routing algorithm and falls into 
the group of interior routing protocols, operating within a single autonomous 
system (AS). OSPF is perhaps the most widely used interior gateway protocol (IGP)
in large enterprise networks. IS-IS, another link-state dynamic routing protocol, 
is more common in large service provider networks. The most widely used exterior
gateway protocol is the Border Gateway Protocol (BGP), the principal routing protocol 
between autonomous systems on the Internet.

* Advantages of link state routing (as opposed to distance vector routing) include
  that link state routing converges rather quickly and  
 * is not subject to the count-to-infinity problem; hence, no measures to combat
   this problem need to be taken. As the full network topology 
 * is known to every node, rather advanced routing techniques can be implemented. 
* Disadvantages include that the link state information needs to be flooded through
   the network, causing higher overhead than link state protocols. 
 * The memory and computational requirements are also higher.

OSPF is an interior gateway protocol that routes Internet Protocol (IP) packets 
solely within a single routing domain (autonomous system). It gathers link state 
information from available routers and constructs a topology map of the network.
 The topology determines the routing table presented to the Internet Layer which
 makes routing decisions based solely on the destination IP address found in IP packets.
 OSPF was designed to support variable-length subnet masking (VLSM) or Classless 
 Inter-Domain Routing (CIDR) addressing models.
'''
class Graph:
    #the keys are the nodes and values are the link
    def __init__(self):
        #create an initial empty graph
        self._structure = dict()
    def __str__(self):
        strnodes="\nNodes"
        for v in self._structure:
            strnodes +="\t"+str(v)
        links=self.links()
        strlink="\nLinks:"
        for w in links:
            strlink +=str(w)
        return ("Total Nodes: " +str(self.num_nodes())+"\n"+"Total Links: "+
                               str(self.num_links())+ strnodes+strlink)
    #ADT methods to query the graph

    def num_nodes(self):
        return len(self._structure)

    def num_links(self):
        num = 0
        for v in self._structure:
            num +=len(self._structure[v])
        return num // 2

    def nodes(self):
        return [key for key in self._structure]

    def get_node_by_label(self, element):
        for v in self._structure:
            if v.element()== element:
                #print(v)
                return v
        return None
    def links(self):
        linklist = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates,only return if v in the first nodes
                if self._structure[v][w].start() ==v:
                    linklist.append(self._structure[v][w])
        return linklist
        
    def get_links(self,v):
        #list of all links
        if v in self._structure:
            linklist = []
            for w in self._structure[v]:
                linklist.append(self._structure[v][w])
            return linklist
        return None

    def get_link(self,v,w):
        #link between v and w
        if(self._structure != None and v in self._structure
           and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        #return degree of node v
        return len(self._structure[v])

    def get_weight(self,v,w):
        #Cost between v and w
        if(self._structure !=None and v in self._structure
            and w in self._structure[v]):
            return len(self._structure[v][w])

    def add_node(self,element):
        v=Node(element)
        self._structure[v]=dict()
        return v

    
    def add_node_if_new(self, element):
        for v in self._structure:
            if v.element()== element:
                #print("already there")
                return v
        return self.add_node(element)

    def add_link(self, v, w,element):
        if not v in self._structure or not w in self._structure:
            return None
        e=Link(v,w,element)
        self._structure[v][w]=e
        self._structure[w][v]=e
        return e

    def highestdegreenode(self):
        #return the vertex with highet degree
        hd=-1
        hdv=None
        for v in self._structure:
            if self.degree(v)>hd:
                hd=self.degree(v)
                hdv = v
        return hdv
    '''dijkstra(s):find all shortest paths from s

            closed starts as an empty dictionary
            locs is an empty dictionary(keys are nodes,values are location open)
            preds starts as a dictionary with value for s=None
            open starts as an empty APQ
            add s with APQ key 0 to open and s:(returned elt) to locs
            ##add s with key 0 to open and put the returned element as value for s in locs
            
            while open is not empty
                remove tha min element v and its key from open
                remove the entry for v from locs and from preds
                add an entry for v with cost and predecessor into closed
                for each edge e from v
                    w is the opposite node/vertex to v on e
                    if w is not in closed
                        newcost is v's key plus e's cost
                        if w is not in loctions
                           add w:v to predes,and newcost:w to open, add
                                           w:(returned elt from open)to locs
                        else if newcost is better than w's oldcost
                            update w:v in preds,update w's cost in open to newcost
            return closed
    '''
    def linkState(self, src):
        closed = dict()
        locs = dict()
        pred = {src:None}
        apq = APQHeap()#empty apq
        locs[src]=apq.add(0,src)
        while not apq.is_empty():
            key, u = apq.remove_min()
            del locs[u]
            closed[u]=(key,pred[u])
            for e in self.get_links(u):
                v = e.opposite(u)
                if v not in closed:
                    newcost = e.element() + key
                    if v not in locs:
                        pred[v] = u
                        locs[v] = apq.add(newcost,v)
                    elif newcost< apq.get_key(locs[v]):
                        pred[v] = u
                        apq.update_key(locs[v],newcost)
        return closed

    def graphreader(filename):
         
        """ Read and return the route map in filename. """
        graph = Graph()
        file = open(filename, 'r')
        entry = file.readline() #either 'Node' or 'Edge'
        num = 0
        print("**********Welcome to Link State Topology*************")
        while entry == 'Node\n':
            num += 1
            nodeid = int(file.readline().split()[1])
            node = graph.add_node(nodeid)
            entry = file.readline() #either 'Node' or 'Edge'
        print("\tFound", num, 'Nodes and added into the graph')
        num = 0
        while entry == 'Edge\n':
            num += 1
            source = int(file.readline().split()[1])
            sv = graph.get_node_by_label(source)
            target = int(file.readline().split()[1])
            tv = graph.get_node_by_label(target)
            length = float(file.readline().split()[1])
            edge = graph.add_link(sv, tv, length)
            file.readline() #read the one-way data
            entry = file.readline() #either 'Node' or 'Edge'
        print("\tFound", num, 'Links and added into the graph')
        print(graph)
        return graph
