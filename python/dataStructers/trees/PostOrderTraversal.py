class Tree:
  def __init__(self,value):
    self.value=value
    self.leftChild=None
    self.rightChild=None
    
new=Tree("drinks")
hot=Tree("hot")
soft=Tree("cold")
new.leftChild=hot
new.rightChild=soft

def PostorderTraversal(rootnode):
  if not rootnode:
    return
  InorderTraversal(rootnode.leftChild)
  InorderTraversal(rootnode.rightChild)
  print(rootnode.value)

PostorderTraversal(new)
