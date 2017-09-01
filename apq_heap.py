#!/usr/bin/python3
#author:Hamid.19-07-2017
class APQHeap:
    """ Maintain an collection of items, popping by lowest key.

        This implementation maintains the collection using a binary heap.
        Keys and or values can be updated.
        Items can be arbitrarily removed.
    """
    class Element:
        """ An element with a key and value and an index to the heap-array. """
        
        def __init__(self, k, v, index):
            self._key = k
            self._value = v
            self._index = index

        def __eq__(self, other):
            """ Return True if this key equals the other key. """
            return self._key == other._key

        def __lt__(self, other):
            """ Return True if this key is less than the other key. """
            return self._key < other._key

        def _wipe(self):
            """ Set the instance variables to None. """
            self._key = None
            self._value = None
            self._index = None

    def __init__(self):
        """ Create an APQ with no elements. """
        self._heap = []
        self._size = 0
        
    def __str__(self):
        """ Return a breadth-first string of the values. """
        outstr = '<-'
        for elt in self._heap:
            outstr += str(elt._value) + ':' + str(elt._key) + '-'
        return outstr + '<'

    def add(self, key, value):
        """ Add Element(key,value,size) to the heap. """
        e = APQHeap.Element(key, value, self._size)
        self._heap.append(e)
        self._upheap(self._size)
        self._size += 1
        return e

    def min(self):
        """ Return the min priority key,value. """
        if self._size:
            return self._heap[0]._key, self._heap[0]._value
        return None, None

    def _swap_last_into_place(self, topos):
        """ Swap the last item into position topos. """
        if self._size > 1: #if other items, restructure
            self._heap[topos] = self._heap[self._size - 1]
            self._heap[topos]._index = topos
            self._heap.pop()
            self._size -= 1
            parent = self._parent(topos)
            if parent > -1 and self._heap[topos]._key < self._heap[parent]._key:
                self._upheap(topos)
            else:
                self._downheap(topos)
        else:
            self._heap.pop()
            self._size -= 1
            
    def remove_min(self):
        """ Remove and return the min priority key,value. """
        returnvalue = None
        returnkey = None
        if self._size:
            returnkey = self._heap[0]._key
            returnvalue = self._heap[0]._value
            self._heap[0]._wipe()
            self._swap_last_into_place(0)
        return returnkey, returnvalue

    def length(self):
        """ Return the number of items in the heap. """
        return self._size

    def is_empty(self):
        """ Return True if the heap is empty. """
        return self._size == 0

    def _left(self, posn):
        """ Return the index of the left child of elt at index posn. """
        return 1 + 2*posn

    def _right(self, posn):
        """ Return the index of the right child of elt at index posn. """
        return 2 + 2*posn

    def _parent(self, posn):
        """ Return the index of the parent of elt at index posn. """
        return (posn - 1)//2
    
    def _upheap(self, posn):
        """ Bubble the item in posn in the heap up to its correct place. """
        if posn > 0 and self._upswap(posn, self._parent(posn)):
            self._upheap(self._parent(posn))

    def _upswap(self, posn, parent):
        """ If healp elt at posn has lower key than parent, swap. """
        if self._heap[posn] < self._heap[parent]:
            self._heap[posn], self._heap[parent] = self._heap[parent], self._heap[posn]
            self._heap[posn]._index = posn
            self._heap[parent]._index = parent
            return True
        return False

    def _downheap(self, posn):
        """ Bubble the item in posn in the heap down to its correct place. """
        #find minchild position
        #if minchild is in the heap
        #    if downswap with minchild is true
        #        downheap minchild
        minchild = self._left(posn)
        if minchild < self._size:
            if (minchild + 1 < self._size and
                self._heap[minchild]._key > self._heap[minchild + 1]._key):
                minchild +=1
            if self._downswap(posn, minchild):
                self._downheap(minchild)

    def _downswap(self, posn, child):
        """ If healp elt at posn has lower key than child, swap. """
        #Note: this could be merged with _upswap to provide a general
        #heapswap(first, second) method, which swaps if the element
        #first has lower key than the element second
        if self._heap[posn]._key > self._heap[child]._key:
            self._heap[posn], self._heap[child] = self._heap[child], self._heap[posn]
            self._heap[posn]._index = posn
            self._heap[child]._index = child
            return True
        return False

    def update_key(self, location, key):
        """ Update the key of the item in location. """
        #location is actually an Element
        #updating the key may require us to rebalance the heap
        location._key = key
        parent = self._parent(location._index)
        if parent > -1 and location._key < self._heap[parent]._key:
            self._upheap(location._index)
        else:
            self._downheap(location._index)

    def update_value(self, location, value):
        """ Update the value of the item in location. """
        #location is actually an Element
        location._value = value
        
    def get_key(self, location):
        """ Return the current key (priority value) for item in location. """
        #location is actually an Element
        return location._key

    def remove(self, location):
        """ Remove the item in location from the APQ, and return key,value. """
        #location is actually an Element
        returnkey = location._key
        returnvalue = location._value
        pos = location._index
        self._swap_last_into_place(pos)
        location._wipe()
        location = None
        return returnkey, returnvalue

    def _printstructure(self):
        """ Print out the elements one to a line. """
        for elt in self._heap:
            if elt is not None:
                print('(', elt._key, ',', elt._value, ',', elt._index, ')')
            else:
                print('*')

    
    
    



