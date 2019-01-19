#arbitrarily defined as 256 by 256
import numpy as np

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
# import numpy as np
# if __name__ == "__main__":
#    a = np.array([[1,1,1,1,0,1],[0,0,1,1,1,0],[0,1,1,1,0,1],[0,1,1,1,1,0],[0,1,1,1,0,1],[0,1,1,1,1,1]])
#    getClusters(a)