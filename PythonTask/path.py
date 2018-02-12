import numpy as np
matrix = np.random.randint(10, size=(5, 5))
print(matrix);

i=0;
j=0;
shortestPath = [];
while "true":
    if i >= 5:
        break;
    center = int(matrix[i][j]);

    nearElements = [];

    top = 0;
    if i > 0:
        nearElements.append([i - 1, j, (matrix[i - 1][j])]);
        top = (matrix[i - 1][j]);

    bottom = 0;
    if i < 4:
        nearElements.append([i + 1, j, (matrix[i + 1][j])]);
        bottom = (matrix[i + 1][j]);

    right = 0;
    if j < 4:
        nearElements.append([i, j + 1, (matrix[i][j + 1])]);
        right = (matrix[i][j + 1]);

    left = 0;
    if j != 0:
        nearElements.append([i, j - 1, (matrix[i][j - 1])]);
        left = (matrix[i][j - 1]);

    for idxI in range(len(nearElements)):
        twoElementSum = center + nearElements[idxI][2];
        for idxJ in range(idxI + 1, len(nearElements)-1):
            tempSum = center + nearElements[idxI][2] + nearElements[idxJ][2];
            if tempSum == 21:
                print("****************************************");
                print ("Path that sums up to 21: ");
                print(center," (",i,",", j,")");
                print(nearElements[idxI][2]," (" ,nearElements[idxI][0],",", nearElements[idxI][1],")");
                print(nearElements[idxJ][2]," (", nearElements[idxJ][1],",", nearElements[idxJ][2],")");
                print("****************************************");
                if not shortestPath:
                    shortestPath.append([i, j, center]);
                    shortestPath.append([nearElements[idxI][0], nearElements[idxI][1], nearElements[idxI][2]]);
                    shortestPath.append([nearElements[idxJ][0], nearElements[idxJ][1], nearElements[idxJ][2]]);

                for idxK  in range(j + 1,len(nearElements) - 1):
                    fourSum = center + nearElements[idxI][2] + nearElements[idxJ][2] + nearElements[idxK][2];
                    if fourSum == 21:
                        print();
                        print ("Path that sums up to 21: ");
                        print(center," (",i,",", j,")");
                        print(nearElements[idxI][2]," (" ,nearElements[idxI][0],",", nearElements[idxI][1],")");
                        print(nearElements[idxJ][2]," (", nearElements[idxJ][1],",", nearElements[idxJ][2],")");
                        print(nearElements[idxK][2]," (", nearElements[idxK][1],",", nearElements[idxK][2],")");

                        if not shortestPath:
                            shortestPath.append([i, j, center]);
                            shortestPath.append([nearElements[idxI][0], nearElements[idxI][1], nearElements[idxI][2]]);
                            shortestPath.append([nearElements[idxJ][0], nearElements[idxJ][1], nearElements[idxJ][2]]);
                            shortestPath.append([nearElements[idxK][0], nearElements[idxK][1], nearElements[idxK][2]]);

    j+=1
    if j == 5:
        i+=1;
        j = 0;

if len(shortestPath)>0:
    print ("Shortest path ");
    for idx in range(0,len(shortestPath)):
        print (shortestPath[idx][2] , "(", shortestPath[idx][0],",",shortestPath[idx][1],")");
else:
    print ("No path found that sums up to 21");