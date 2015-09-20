#This program allows you to play a game of snake on 
#BlinkyTape
import numpy as np

#matplotlib shows an alternative
#view of the game baord
import matplotlib.pyplot as plt
import matplotlib.cm as cm

board = np.zeros((25,7))
plt.imshow(board, cmap = cm.Greys_r, interpolation="none")
plt.show()
