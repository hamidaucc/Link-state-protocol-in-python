# Link-state-protocol-in-python
This project implenments the OSPF using Dijkstra algorithm (Open Shortest Path First) network protocol in python.   Link-State Routing protocol is a main class of routing protocols.  It is performed by every switching node/router in the network.  The basic concept of link-state routing is that every node  constructs a map of the connectivity to the network, in the  form of a Graph, showing which nodes are connected to which  other nodes. Each node then independently calculates the next  best logical path from it to every possible destination in the network.  The collection of best paths will then form the node's routing table. OSPF: ----- Open Shortest Path First (OSPF) is a link-state routing protocol for Internet  Protocol (IP) networks. It uses a link state routing algorithm and falls into  the group of interior routing protocols, operating within a single autonomous  system (AS). OSPF is perhaps the most widely used interior gateway protocol (IGP) in large enterprise networks. IS-IS, another link-state dynamic routing protocol,  is more common in large service provider networks. The most widely used exterior gateway protocol is the Border Gateway Protocol (BGP), the principal routing protocol  between autonomous systems on the Internet.  * Advantages of link state routing (as opposed to distance vector routing) include   that link state routing converges rather quickly and    * is not subject to the count-to-infinity problem; hence, no measures to combat    this problem need to be taken. As the full network topology   * is known to every node, rather advanced routing techniques can be implemented.  * Disadvantages include that the link state information needs to be flooded through    the network, causing higher overhead than link state protocols.   * The memory and computational requirements are also higher.  OSPF is an interior gateway protocol that routes Internet Protocol (IP) packets  solely within a single routing domain (autonomous system). It gathers link state  information from available routers and constructs a topology map of the network.  The topology determines the routing table presented to the Internet Layer which  makes routing decisions based solely on the destination IP address found in IP packets.  OSPF was designed to support variable-length subnet masking (VLSM) or Classless   Inter-Domain Routing (CIDR) addressing models.
