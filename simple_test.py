try:
	from nrgten.encom import ENCoM
except ImportError as e:
	print("NRGTEN is not installed on your machine. To install, run the following command:\npip install nrgten")
	raise e
	
if __name__ == "__main__":
	model = ENCoM("test_medium.pdb")
	diff = abs(504.8449418766389 - model.compute_vib_entropy())
	if diff < 0.00001:
		print("NRGTEN is properly installed on your system!")
	else:
		raise ValueError("NRGTEN seems installed on your system, but does not give the proper value for this test...")
