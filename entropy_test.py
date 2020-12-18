try:
	from nrgten.encom import ENCoM
except ImportError as e:
	print("NRGTEN is not installed on your machine. To install, run the following command:\npip install nrgten")
	raise e

if __name__ == "__main__":
	wt = ENCoM("6r74.pdb")
	tyr103 = ENCoM("6r74_TYR103.pdb")
	wt_entropy = wt.compute_vib_entropy(beta=1)
	tyr103_entropy = tyr103.compute_vib_entropy(beta=1)
	diff_entropy = wt_entropy - tyr103_entropy
	print(diff_entropy)