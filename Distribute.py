import math
from operator import itemgetter
def distributeNodes(NodeList, NumOfSwarms):
    NodeList = sortNodeList(NodeList)
    NodeLenList = []
    for NodeIndex in range(len(NodeList)-1):
        #may be expensive
        NodeLenList.append(math.sqrt((NodeList[NodeIndex][0] - NodeList[NodeIndex+1][0])**2 +
                          (NodeList[NodeIndex][1] - NodeList[NodeIndex+1][1])**2))
    swarmPlacement = sum(NodeLenList)/(NumOfSwarms-1)
    swarmGoals = []
    for swarmElNum in range(NumOfSwarms):
        swarmGoals.append(setSwarms(swarmPlacement, swarmElNum,NodeLenList, NodeList))

    return swarmGoals


def setSwarms(f, x, NodeLenList, NodeList):
    fx = f*x
    index = 0
    while(not(math.isclose(fx,NodeLenList[index])) and fx > NodeLenList[index]):
        fx -= NodeLenList[index]
        index+=1
    if (math.isclose(fx,NodeLenList[index])):
        return NodeList[index+1]
    else:
        theta = math.acos((NodeList[index+1][0]-NodeList[index][0])/NodeLenList[index])
        thetaDeg = theta*180/math.pi
        return [round((NodeList[index][0] +fx*math.cos(theta)),5), round(NodeList[index][1] + fx*math.sin(theta),5)]


def sortNodeList(NodeList):
    NodeList.sort(key=itemgetter(0))
    return NodeList

