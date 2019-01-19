import math
from operator import itemgetter
def distributeNodes(NodeList, NumOfSwarms):
    NodeList = sortNodeList(NodeList)
    NodeLenList = []
    for NodeIndex in range(len(NodeList)-1):
        #may be expensive
        NodeLenList.append(math.sqrt((NodeList[NodeIndex][0] - NodeList[NodeIndex+1][0])**2 +
                          (NodeList[NodeIndex][1] - NodeList[NodeIndex+1][1])**2))
    swarmPlacement = sum(NodeLenList)/NumOfSwarms
    swarmGoals = []
    for swarmElNum in range(NumOfSwarms):
        swarmGoals.append(setSwarms(swarmPlacement, swarmElNum+1,NodeLenList, NodeList))


def setSwarms(f, x, NodeLenList, NodeList):
    fx = f*x
    index = 0
    while(fx > NodeLenList[index]):
        fx -= NodeLenList(index)
        index+=1
    if (fx == NodeLenList[index]):
        return NodeList[index+1]
    else:
        theta = math.acos((NodeList[index][0]-NodeList[index+1][0])/NodeLenList[index])
        return [fx*cos(theta), fx*sin(theta)]


def sortNodeList(NodeList):
    NodeList.sort(key=itemgetter(0))
    return NodeList

