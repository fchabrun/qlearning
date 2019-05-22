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
# game state (win, lose)

MAX_TURNS=100
MAX_SPEED=.2
COLLISION_DISTANCE=.1
#X_LIM=(0,10)
#Y_LIM=(0,10)

# create empty states list
state = np.array([]).reshape((0,9))
# create initial state
initial_state = np.array([[1,1, 9,1, 1,9, 9,9, 0]])

# add new initial state to states
state=np.concatenate((state, initial_state),axis=0)

def distance(x1,y1,x2,y2):
    return np.sqrt(np.power(x2-x1,2)+np.power(y2-y1,2))

def applyAngleAndSpeed(cur_x,cur_y,chosen_angle,chosen_speed):
    final_speed=np.minimum(1, np.abs(chosen_speed))
    new_x=cur_x+np.sin(chosen_angle)*final_speed
    new_y=cur_y+np.cos(chosen_angle)*final_speed
    new_x=np.minimum(10, np.maximum(0, new_x))
    new_y=np.minimum(10, np.maximum(0, new_y))
    return new_x, new_y

def enemyAI(x1,y1,x2,y2):
    total_distance=distance(x1,y1,x2,y2)
    limit_factor=MAX_SPEED/total_distance
    return x1+(x2-x1)*limit_factor, y1+(y2-y1)*limit_factor

def heroAI(cur_state):
    # random play
    # select random angle
    # select random speed
    a = np.random.random()*np.pi
    s = np.random.random()*MAX_SPEED
    return a, s

def playTurn(state):
    # get previous state
    cur_state=state[-1]
    # escape if status == over
    if cur_state[8] != 0:
        return np.concatenate((state, cur_state.reshape((1,cur_state.shape[0]))),axis=0)
    # initialize next step
    new_state=cur_state.copy()
    # make hero turn
    a,s=heroAI(cur_state)
    new_state[0:2]=applyAngleAndSpeed(cur_state[0],cur_state[1],a,s)
    # make enemies play
    new_state[2:4]=enemyAI(cur_state[2],cur_state[3],cur_state[0],cur_state[1])
    new_state[4:6]=enemyAI(cur_state[4],cur_state[5],cur_state[0],cur_state[1])
    # check win/lose state
    game_state=0
    if distance(new_state[0],new_state[1],new_state[2],new_state[3]) < COLLISION_DISTANCE:
        game_state=-1
    elif distance(new_state[0],new_state[1],new_state[4],new_state[5]) < COLLISION_DISTANCE:
        game_state=-1
    elif distance(new_state[0],new_state[1],new_state[6],new_state[7]) < COLLISION_DISTANCE:
        game_state=1
    new_state[8]=game_state
    # add state to states list
    return np.concatenate((state, new_state.reshape((1,new_state.shape[0]))),axis=0)

for i in range(MAX_TURNS-1):
    state=playTurn(state)

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

# maintenant, on peut analyser la liste des récompenses

# on va commencer par retirer les dernières frames (répétitions = inutiles)
trainset=state[:(np.where(state[:,8]!=0)[0][0]+1),:]

# on peut alors calculer les discounted reward
discounted_rewards=np.zeros((trainset.shape[0]))
gamma=.9
n=trainset.shape[0]
final_reward=trainset[-1,8]
for i in range(trainset.shape[0]):
    discounted_rewards[i]=np.power(gamma,n-(i+1))*final_reward
    
# maintenant on peut entraîner notre AI




