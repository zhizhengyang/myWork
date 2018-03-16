import os
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from xml.dom.minidom import parse
import xml.dom.minidom

def read_xml(in_path):
  tree = ElementTree()
  tree.parse(in_path)
  return tree
 
def write_xml(tree, out_path):
  tree.write(out_path, encoding="utf-8",xml_declaration=True)
 
def if_match(node, kv_map):
  for key in kv_map:
    if node.get(key) != kv_map.get(key):
      return False
  return True

def find_nodes(tree, path):
    return tree.findall(path)

def get_node_by_keyvalue(nodelist, kv_map):
  result_nodes = []
  for node in nodelist:
    if if_match(node, kv_map):
      result_nodes.append(node)
  return result_nodes

def change_node_properties(nodelist, kv_map, is_delete=False):
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))
    
def xmlJx(filePath=''):
    DOMTree = loadXMLDoc(filePath)
    collection = DOMTree.getElementsByTagName('filename')
    collection=collection[0]
    collection.set('filename','test')
    x=collection.firstChild
    x.nodevalue='test'
    document.write(x)

def renameFile(filepath=''):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        num=allDir.split('.')[0]
        rest=6-len(num)
        if rest>0:
            a=''
            for i in range(rest):
                a=a+'0'
        fileName=a+allDir
        os.rename(filepath+'/'+allDir,filepath+'/'+fileName)

def delteFile(filePath=''):
    pathDir =  os.listdir(filePath)
    for allDir in pathDir:
        num=allDir.split('.')[1]
        if num=='xml':
            os.remove(filePath+'/'+allDir)

            

xmlJx('mark/000002.xml')
