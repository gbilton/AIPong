import numpy as np

from classes import createaxes, plotaxes


limite = 10

points = np.load('points.npy')
limits = np.ones(len(points)) * limite
losses = np.load('losses.npy', allow_pickle=True)
avgtime = np.load('avgtime.npy')
avgscore = np.load('avgscore.npy')

fig, ax1, ax2, ax3 = createaxes()
plotaxes(fig, ax1, ax2, ax3, points, limits, losses, avgtime, avgscore)
