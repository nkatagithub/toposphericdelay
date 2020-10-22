import math

#TODO var list(td, dd, dw, melv, h, elev)
#TODO topospheric delay
#m(elev) = melv
# TODO ddry
# TODO unknown vars(h> height above sea level, elev> elevation)

elevations = [4.60397339, 9.59394836, 14.7786942, 25.5419617, 36.4652672, 51.7901459, 56.1026764, 62.1996498, 63.2208443]
h = int(2439.1540)
dd = int(2.3)*math.exp(int(0.116103)*h)
dw = int(0.1)
tdlst = []
for elev in elevations:
	melev = int(1.001)/math.sqrt(int(0.002001) + math.sin(elev)**2)
	td = (dd+dw)*melev
	tdlst.append(td)
	print(td)
