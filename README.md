# Flappy-Bird

Made by: Jon Pryzby
Last Updated: 3/19/2021
Primary language: Python

##################################################################
###                                                            ###
###  Run this program at https://trinket.io/python/3f36c6546f  ###
###                                                            ###
##################################################################

A non-player character playing a flappy bird inspired game.

A class pipe is declared as an object with a pipe image, a set of x and y coordinates, and a constant negative speed. Once per game tick, the wall object's coordinates are shifted by an amount proporional to its speed.

A class birb is declared as an object with a bird image, a set of x and y coordinates, and a y velocity. Once per game tick, the birb's speed is changed based on a physics function, and whether or not they chose to flap. The birb object's coordinates are shifted by an amount proportional to its speed

The player has one input, the space bar, which calls a flap() function, that gives the birb object a positive velocity. For the sake of this demo, control is given to an AI. To disable AI and play the game manaully, simply comment out the following line
"AI()"