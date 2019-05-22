# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:10:49 2019

@author: hit47
"""

import numpy as np

# un état a les variables suivantes :
# hero_x
# hero_y
# enemy1_x
# enemy1_y
# enemy2_x
# enemy2_y
# goal_x
# goal_y

MAX_TURNS=100
MAX_SPEED=.2

# create empty states list
state = np.array([]).reshape((0,8))
# create initial state
initial_state = np.array([[1,1, 9,1, 1,9, 9,9]])

# add new initial state to states
state=np.concatenate((state, initial_state),axis=0)

# run a random turn
def random_turn(state):
    cur_state=state[-1,...]
    cur_x=cur_state[0]
    cur_y=cur_state[1]
    next_x=np.minimum(10,np.maximum(0,cur_x+(np.random.random()-.5)/5))
    next_y=np.minimum(10,np.maximum(0,cur_y+(np.random.random()-.5)/5))
    new_state = cur_state.copy()
    new_state[0]=next_x
    new_state[1]=next_y
    # add state to states list
    return np.concatenate((state, new_state.reshape((1,8))),axis=0)

def distance(x1,y1,x2,y2):
    return np.sqrt(np.power(x2-x1,2)+np.power(y2-y1,2))

def limitSpeed(x1,y1,x2,y2):
    total_distance=distance(x1,y1,x2,y2)
    limit_factor=MAX_SPEED/total_distance
    
    np.sin()

def heroAI(cur_state):
    # random turn
    cur_x=cur_state[0]
    cur_y=cur_state[1]
    next_x=np.minimum(10,np.maximum(0,cur_x+(np.random.random()-.5)/5))
    next_y=np.minimum(10,np.maximum(0,cur_y+(np.random.random()-.5)/5))
    return next_x, next_y

def playTurn(state):
    cur_state=state[-1]
    # make hero turn
    new_state=cur_state.copy()
    new_state[0:2]=heroAI(cur_state)
    # make enemies play
    cur_state[2]
    cur_state[3]
    
    
    
    # add state to states list
    return np.concatenate((state, new_state.reshape((1,8))),axis=0)
    

for i in range(MAX_TURNS-1):
    state=random_turn(state)

# Make animation

from matplotlib.pyplot import plot, show, subplots
import matplotlib.animation as animation

fig,ax=subplots(figsize=(6,6))
ax.set_xlim([0,10])
ax.set_ylim([0,10])

def animate(i):
    animlist = plot(state[i][0],state[i][1],'b',
                    state[i][2],state[i][3],'r',
                    state[i][4],state[i][5],'r',
                    state[i][6],state[i][7],'g',
                    marker='o',markersize=8)
    return animlist

def init():
    return []

anim=animation.FuncAnimation(fig,animate,frames=state.shape[0],interval=20,init_func=init,blit=True,repeat=0)
show()
