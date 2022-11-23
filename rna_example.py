from nrgten.encom import ENCoM
import numpy as np

wt = ENCoM("mir125a_WT.pdb")
g22u = ENCoM("mir125a_G22U.pdb")

entrosig_wt = wt.compute_bfactors_boltzmann(beta=np.e**2.25)
entrosig_g22u = g22u.compute_bfactors_boltzmann(beta=np.e**2.25)
