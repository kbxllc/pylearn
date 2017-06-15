def convertstring(x):
	""" Converts passed in str to int.
    :param x: str.
    :return: string converted to an int.
    """
	try:
		return float(x)
	except ValueError:
		print("Wrong value dummy")


d = convertstring("yellow")
print(d)