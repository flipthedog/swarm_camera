#arbitrarily defined as 256 by 256
import numpy as np
import math
import Distribute
import Visualization

def getClusters(npImage):
    #prolly got my x and y's mixed up
    xlen, ylen = npImage.shape
    isClustered = np.zeros((xlen,ylen))
    clusterList = []
    for y in range(len(npImage[0,:])):
        for x in range(len(npImage[:,0])):
            if isClustered[x,y] == 0 and npImage[x,y] == 0:
                clusterList.append(clusterHere(npImage,isClustered, [[x,y]], [], xlen, ylen))
    print ("herelol")
    return clusterList

def clusterHere(npImage,isClustered, queue, cluster, xlen, ylen):

    while len(queue) != 0:
         point = queue.pop()
         if(npImage[point[0], point[1]] == 0):
            cluster.append(point)
         isClustered[point[0],point[1]] = 1
         for x in range(3):
             x -= 1
             for y in range(3):
                 y -= 1
                 if not ((point[0]+x < 0 or point[0]+x >= xlen) or
                     (point[1] + y < 0 or point[1] + y >= ylen)):
                     if(npImage[point[0], point[1]] == 0) and (isClustered[point[0]+x, point[1]+y] == 0) and ([point[0]+x, point[1]+y] not in queue):
                         queue.append([point[0]+x, point[1]+y])
                     elif (npImage[point[0], point[1]] != 0) and (npImage[point[0]+x, point[1]+y] == 0) and (isClustered[point[0]+x, point[1]+y] == 0) and ([point[0]+x, point[1]+y] not in queue):
                         queue.append([point[0]+x, point[1]+y])


    return cluster


def clusters(swarmbois):
    npImage = np.array([[1,1,1,1,0,1],[0,0,1,1,1,0],[0,1,1,1,0,1],[0,1,1,1,1,0],[0,1,1,1,0,1],[0,1,1,1,1,1]])
    setOfClusters = getClusters(npImage)
    clustercentroids = []
    clusterProportion = 0
    for cluster in setOfClusters:
        clustercentroids.append([sum([pair[0] for pair in cluster])/len(cluster), sum([pair[1] for pair in cluster])/len(cluster)])
        clusterProportion += len(cluster)
    clusterProportion /= len(swarmbois)
    numInDict = dict()

    for clustindex in range(len(setOfClusters)):
        numInDict[clustindex] = math.ceil(len(setOfClusters[clustindex])/clusterProportion)
    clusterdict = dict()

    for boi in swarmbois:
        manhat = abs(clustercentroids[0][0]-boi.x) + abs(clustercentroids[0][1]-boi.y)
        inde = 0
        for i in range(len(clustercentroids)):
            if numInDict[i] > 0 and abs(clustercentroids[i][0]-boi.x) + abs(clustercentroids[i][1]-boi.y) < manhat:
                manhat = abs(clustercentroids[i][0]-boi.x) + abs(clustercentroids[i][1]-boi.y)
                inde = i
        if inde not in clusterdict:
            clusterdict[inde] = [boi]
        else:
            clusterdict[inde].append(boi)
        numInDict[inde]-=1

    setPoints = []
    for index in range(len(swarmbois)):
        setPoints.append([-1,-1])
    for key, val in clusterdict.items():

        points = Distribute.distributeNodes(setOfClusters[key], len(val))
        for pindx in range(len(points)):
            setPoints[swarmbois.index(val[pindx])] = points[pindx]
    return setPoints

# class Particle:
#
#     def __init__(self, x, y, width, height):
#
#         self.width = width
#         self.height = height
#
#         self.x = x
#         self.y = y
#         self.vy = 0
#         self.vx = 0
#         self.ax = 0
#         self.ay = 0
#         self.goalx = x
#         self.goaly = y
#         self.velocity_mag = 0.5 # Speed of the particles
#
#     def setGoal(self, x,y):
#         self.goalx = x
#         self.goaly = y
#
# # import numpy as np
# if __name__ == "__main__":
#
#     a = [Particle(1,1,1,1),Particle(0,0,1,1),Particle(2,2,1,1),Particle(5,5,1,1),Particle(8,8,1,1),Particle(3,3,1,1)]
#     clusters(a)