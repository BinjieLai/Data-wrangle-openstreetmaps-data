#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""




def process_map(filename):
    """
    interparses file and counts the number of unique user IDs ("uid")
    Args:
        filename: the path of import file
    Returns:
        a set of unique user IDs ("uid")    
    """
    users = set()
    for _, element in ET.iterparse(filename):
        #print element.tag
        if element.tag == "node" or element.tag == "way" or element.tag == "relation":
        #print element.attrib['uid']
            users.add(element.attrib['uid'])
            
        pass

    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()