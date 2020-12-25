from nrgten.enm import ENM
import random
import numpy as np
from nrgten.metrics import get_transit_probs

class RNM(ENM):

    def __init__(self, pdb_file, alpha=0.5, kr=1, solve=True, use_pickle=False,
                 ignore_hetatms=False, atypes_list=None, massdef_list=None,
                 solve_mol=True, one_mass=False):
       self.alpha = alpha # the interaction probability
       self.kr = kr # the spring constant
       super().__init__(pdb_file, solve=solve, use_pickle=use_pickle,
                        ignore_hetatms=ignore_hetatms, atypes_list=atypes_list,
                        massdef_list=massdef_list, solve_mol=solve_mol,
                        one_mass=one_mass)

    def build_hessian(self):
        if not self.mol.solved:
            self.mol.solve()
        masscoords = self.mol.masscoords
        distmat = self.mol.distmat
        n = len(masscoords)
        hessian = np.zeros((3*n, 3*n))
        for i in range(n):
            for j in range(i+1, n):
                if random.uniform(0, 1) <= self.alpha:
                    dist_squared = distmat[i][j] ** 2

                    # diagonal of the off-diagonal 3x3 element and update diagonal of diagonal element
                    for k in range(3):
                        val = 2 * self.kr * (masscoords[j][k] - masscoords[i][k]) ** 2 / dist_squared
                        hessian[3 * i + k][3 * j + k] = -val
                        hessian[3 * i + k][3 * i + k] += val
                        hessian[3 * j + k][3 * j + k] += val

                    # off-diagonals of the off-diagonal 3x3 element and update off-diagonal of diagonal element
                    for (k, l) in ((0, 1), (0, 2), (1, 2)):
                        val = 2 * self.kr * (masscoords[j][k] - masscoords[i][k]) * \
                              (masscoords[j][l] - masscoords[i][l]) / dist_squared
                        hessian[3 * i + k][3 * j + l] = -1 * val
                        hessian[3 * i + l][3 * j + k] = -1 * val
                        hessian[3 * i + k][3 * i + l] += val
                        hessian[3 * j + k][3 * j + l] += val
        for i in range(3 * n):
            for j in range(i + 1, 3 * n):
                hessian[j][i] = hessian[i][j]
        return hessian

    def build_from_pickle(self):
        pass

    def pickle(self):
        pass

if __name__ == "__main__":
    open_cs = RNM("open_clean.pdb")
    closed_cs = RNM("closed_clean.pdb")
    open_prob, closed_prob = get_transit_probs(open_cs, closed_cs)
    print("open_prob: {}, closed_prob: {}".format(open_prob, closed_prob))



