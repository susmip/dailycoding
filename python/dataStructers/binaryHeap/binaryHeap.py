class heap:
  def __init__(self,size):
    self.customList=[None]*(size+1)
    self.maxsize=size+1 
    self.heapSize=0

def peek(rootNode):
  if not rootNode:
    return "empty"
  else:
    return rootNode.customList[1]
    
def sizeofHeap(rootNode):
  if not rootNode:
    return "empty"
  else:
    return rootNode.heapSize

def levelOrder(rootnode):
  if not rootnode:
    return
  else:
    for i in range(1,rootnode.heapSize+1):
      print(rootnode.customList[i])
def heapifyInsert(rootnode,index,heapType):
  parentindex=int(index/2)
  if index<=1:
    return
  if heapType=="min":
    if rootnode.customList[index]<rootnode.customList[parentindex]:
      temp=rootnode.customList[index]
      rootnode.customList[index]=rootnode.customList[parentindex]
      rootnode.customList[parentindex]=temp
    heapifyInsert(rootnode,parentindex,heapType)
  if heapType=="max":
    if rootnode.customList[index]>rootnode.customList[parentindex]:
      temp=rootnode.customList[index]
      rootnode.customList[index]=rootnode.customList[parentindex]
      rootnode.customList[parentindex]=temp
    heapifyInsert(rootnode,parentindex,heapType)
def insertNode(rootnode,value,heapType):
  if rootnode.heapSize+1==rootnode.maxsize:
    return
  rootnode.customList[rootnode.heapSize+1]=value
  rootnode.heapSize+=1 
  heapifyInsert(rootnode,rootnode.heapSize,heapType)
  return "value inserted"

def deleteEntire(rootnode):
  rootnode.customList=None

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
    
newBinaryItem=heap(5)
insertNode(newBinaryItem,4,"max")
insertNode(newBinaryItem,5,"max")
insertNode(newBinaryItem,2,"max")
insertNode(newBinaryItem,1,"max")
print(levelOrder(newBinaryItem))
extractNode(newBinaryItem,"max")
print(levelOrder(newBinaryItem))
