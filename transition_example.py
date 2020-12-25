try:
	from nrgten.encom import ENCoM
	from nrgten.metrics import get_transit_probs
except ImportError as e:
	print("NRGTEN is not installed on your machine. To install, run the following command:\npip install nrgten")
	raise e

if __name__ == "__main__":
	open_cs = ENCoM("open_clean.pdb")
	closed_cs = ENCoM("closed_clean.pdb")
	prob_open, prob_closed = get_transit_probs(open_cs, closed_cs)
	print("prob_open : {}, prob_closed : {}".format(prob_open, prob_closed))

	open_cs_mut = ENCoM("open_clean_LYS239.pdb")
	closed_cs_mut = ENCoM("closed_clean_LYS239.pdb")
	prob_open_mut, prob_closed_mut = get_transit_probs(open_cs_mut, closed_cs_mut)
	print("prob_open_mut : {}, prob_closed_mut : {}".format(prob_open_mut, prob_closed_mut))
