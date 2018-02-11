from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob

def damped_vibrations(t, A, b, w):
	return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
	t = linspace(0, T, resolution+1)
	u = damped_vibrations(t, A, b, w)
	plt.figure()
	plt.plot(t, u)
	plt.title('A=%g, b=%g, w=%g' % (A, b, w))
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		for filename in glob.glob(os.path.join('static', '*.png')):
			os.remove(filename)

	plotfile = os.path.join('static',str(time.time()) + '.png')
	plt.savefig(plotfile)
	return plotfile
