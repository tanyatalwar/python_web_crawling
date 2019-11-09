from treelib import Node, Tree
import json

with open('result.json') as f:
  data = json.load(f)

# print(data[0]["page"])
# print(data[0]["links"])


tree = Tree()
tree.create_node(data[0]["links"], data[0]["page"])
l = len(data)-1
print(l)
for i in range(0,l):
     tree.create_node(data[i]["links"],data[i]["page"],parent=data[0]["page"])
tree.show()
