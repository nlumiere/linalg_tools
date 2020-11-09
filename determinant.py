# Author: Nick Lumiere (nlumiere)

def det_two_two(mtx):
    return mtx[0][0]*mtx[1][1] - mtx[0][1]*mtx[1][0]

def det(l, mtx):
    if l == 2:
        return det_two_two(mtx)
    deter = 0
    mult = -1
    for j in range(l):
        mtx_copy = []
        for x in mtx:
            tmp = []
            for y in range(len(x)):
                if y != j:
                    tmp.append(x[y])
            mtx_copy.append(tmp)
        mult *= -1

        result = det(l-1, mtx_copy[1:])
        deter += mtx[0][j]*mult*result
    return deter

def compute_det(mtx):
    l = len(mtx)
    return det(l, mtx)