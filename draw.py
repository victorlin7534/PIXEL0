with open("image.ppm","w") as pic:
	pic.write("P3 500 500 255 ")
	for x in range(500):
		for y in range(500):
			if (x * y) % 2 == 0:
				pic.write("255 255 255 ")
			else:
				pic.write("0 0 0 ")