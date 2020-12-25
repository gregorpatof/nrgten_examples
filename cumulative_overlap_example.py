try:
	from nrgten.encom import ENCoM
	from nrgten.metrics import cumulative_overlap
except ImportError as e:
	print("NRGTEN is not installed on your machine. To install, run the following command:\npip install nrgten")
	raise e

if __name__ == "__main__":
	closed_cs = ENCoM("closed_clean.pdb")
	open_cs = ENCoM("open_clean.pdb")
	print("Cumulative overlap 10 modes, from closed to open: {}".format(cumulative_overlap(closed_cs, open_cs, 10)))
	print("Cumulative overlap 10 modes, from open to closed: {}".format(cumulative_overlap(open_cs, closed_cs, 10)))
