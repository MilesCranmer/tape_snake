#This program allows you to play a game of snake on 
#BlinkyTape
import numpy as np

#matplotlib shows an alternative
#view of the game baord
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#dimensions of our blinky surface
leds = 25
tapes = 7

move = {'right':np.array([1,0]),'left':np.array([-1,0]),
			'up':np.array([0,1]),'down':np.array([0,-1])}
#the snake is an array of points, 
#with the head listed first:
start = np.array([int(leds/2.0),int(tapes/2.0)])
snake = [start,start+move['left'],start+2*move['left']]
#current direction of the snake
direc = 'right'

board = np.zeros((7,25))
for point in snake:
	board[point[1],point[0]] = 1
plt.imshow(board, cmap = cm.Greys_r, interpolation="none")
plt.show()