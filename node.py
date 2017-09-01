#!/usr/bin/python3
#author:Hamid.19-07-2017
class Node:
    def __init__(self,element):
        self._element = element

    def __str__(self):
        return str(self._element)
    def __lt__(self,v):
        return self._element < v.element()
    def element(self):
        return self._element
