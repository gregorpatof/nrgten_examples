try:
	from nrgten.encom import ENCoM
	from nrgten.metrics import get_overlaps
except ImportError as e:
	print("NRGTEN is not installed on your machine. To install, run the following command:\npip install nrgten")
	raise e

if __name__ == "__main__":
	closed_cs = ENCoM("closed_clean.pdb")
	open_cs = ENCoM("open_clean.pdb", solve=False) # no need to solve the target
	overlaps = get_overlaps(closed_cs, open_cs, 10)
	print(overlaps)