#!/usr/bin/python3
#author:Hamid.19-07-2017
class Link:

    def __init__(self,v,w,element):
        #create link between node v and w
        self._nodes=(v,w)
        self._element = element
        
    def __str__(self):
        return("\n" + str(self._nodes[0])+"-"+
               str(self._nodes[1])+":"+str(self._element))
    
    def nodes(self):
        return self._nodes

    def start(self):
        return self._nodes[0]

    def end(self):
        return self._nodes[1]

    def opposite(self,v):
        if self._nodes[0]==v:
            return self._nodes[1]
        elif self._nodes[1]==v:
            return self._nodes[0]
        else:
            return None

    def element(self):
        return self._element
