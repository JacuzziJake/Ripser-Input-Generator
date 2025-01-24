import numpy as np

def lp(list1, list2, p):
    """
    Implementation of lp norm between vectors in R^n.
    """
    if len(list1) != len(list2):
        print("Invalid input, please input two vectors of the same dimension.")
    else:
        d = 0
        for i in range(len(list1)):
            d += np.abs(list1[i]-list2[i])**p
        return d**(1/p)

def ripser_input(file, output):
    """
    Input: csv file of row vectors separated by commas.
    Output: Lower-triangular distance matrix of pairwise distances between each pair of points.
    """
    with open(file, 'r+') as f:
        points = []
        for line in f.readlines():
            points.append([float(i) for i in line.split(',')])
    distances = []
    for i in range(len(points)):
        j = 0
        row = []
        while j < i:
            row.append(lp(points[i],points[j],2))
            j += 1
        distances.append(row)
        if i == 0:
            distances.pop(0)
    with open(output, 'w') as o:
        o.write('\n')
        for rows in distances:
            for i in rows:
                o.write(str(i) + " ")
            o.write('\n')
