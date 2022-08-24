try:
	from nrgten.encom import ENCoM
	from nrgten.metrics import pca_ensemble, rmsip, get_pcs_no_rot_tran
except ImportError as e:
	print("NRGTEN is not installed on your machine. To install, run the following command:\npip install nrgten")
	raise e

if __name__ == "__main__":
	insulin_nmr = ENCoM("2lwz.pdb")
	variances, pcs = get_pcs_no_rot_tran(insulin_nmr, proportion_nrt_variance=0.9)
	print(rmsip(pcs, insulin_nmr.eigvecs[6:16]))
