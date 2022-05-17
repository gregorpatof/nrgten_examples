try:
	from nrgten.encom import ENCoM
except ImportError as e:
	print("NRGTEN is not installed on your machine. To install, run the following command:\npip install nrgten")
	raise e
	
if __name__ == "__main__":
	model = ENCoM("test_medium.pdb")
	svib = model.compute_vib_entropy()
	expected = 504.8468148072965
	diff = abs(expected - svib)
	if diff < 0.00001:
		print("NRGTEN is properly installed on your system!")
	else:
		raise ValueError("NRGTEN seems installed on your system, but does not give the proper value for this test. The"+
						 " expected Svib value is {:.6f} and your installation produces {:.6f}.".format(expected,svib) +
						 "If the difference is small enough, you can ignore this message.")
