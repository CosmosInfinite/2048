import random
import math

init_state=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

def move(state,direct):
  trim=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
  if direct=="UP":
    for i in range(4):
      lis=[]
      for j in range(4):
        if state[j][i]!=0:
          lis.append(state[j][i])
      for k in range(len(lis)):
        trim[k][i]=lis[k]
    return trim
  if direct=="LEFT":
    for i in range(4):
      lis=[]
      for j in range(4):
        if state[i][j]!=0:
          lis.append(state[i][j])
      for k in range(len(lis)):
        trim[i][k]=lis[k]
    return trim
  if direct=="DOWN":
    for i in range(4):
      lis=[]
      for j in range(4):
        if state[3-j][i]!=0:
          lis.append(state[3-j][i])
      for k in range(len(lis)):
        trim[3-k][i]=lis[k]
    return trim
  if direct=="RIGHT":
    for i in range(4):
      lis=[]
      for j in range(4):
        if state[i][3-j]!=0:
          lis.append(state[i][3-j])
      for k in range(len(lis)):
        trim[i][3-k]=lis[k]
    return trim

def action(state,direct):
  if direct=="UP":
    for i in range(4):
      for j in range(3):
        if state[j][i]==state[j+1][i] and state[j][i]!=0:
          state[j][i]*=2
          if j+1==3:
            state[j+1][i]=0
          else:
            for z in range(j+1,4):
              if z==3:
                state[z][i]=0
              else:
                state[z][i]=state[z+1][i]
    return state
  if direct=="LEFT":
    for i in range(4):
      for j in range(3):
        if state[i][j]==state[i][j+1] and state[i][j]!=0:
          state[i][j]*=2
          if j+1==3:
            state[i][j+1]=0
          else:
            for z in range(j+1,4):
              if z==3:
                state[i][z]=0
              else:
                state[i][z]=state[i][z+1]
    return state
  if direct=="DOWN":
    for i in range(4):
      for j in range(3):
        if state[3-j][i]==state[2-j][i] and state[3-j][i]!=0:
          state[3-j][i]*=2
          if 2-j==0:
            state[2-j][i]=0
          else:
            for z in range(j+1,4):
              if z==3:
                state[3-z][i]=0
              else:
                state[3-z][i]=state[2-z][i]
    return state
  if direct=="RIGHT":
    for i in range(4):
      for j in range(3):
        if state[i][3-j]==state[i][2-j] and state[i][3-j]!=0:
          state[i][3-j]*=2
          if 2-j==0:
            state[i][2-j]=0
          else:
            for z in range(j+1,4):
              if z==3:
                state[i][3-z]=0
              else:
                state[i][3-z]=state[i][2-z]
    return state

def check_end(state):
  end=True
  for x in range(4):
    for y in range(4):
      if state[x][y]==0:
        end=False
        break
  if end:
    check=[[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]
    for x in range(4):
      for y in range(4):
        check[x+1][y+1]=state[x][y]
    for x in range(1,5):
      for y in range(1,5):
        if check[x][y]==check[x+1][y] or check[x][y]==check[x-1][y] or check[x][y]==check[x][y+1] or check[x][y]==check[x][y-1]:
          end=False
          break
  return end                

def rand_gen(state):
  while True:
    r=random.random()
    if r<=0.3:
      x=0
    elif r<=0.5:
      x=1
    elif r<=0.7:
      x=2
    else:
      x=3
    r=random.random()
    if r<=0.3:
      y=0
    elif r<=0.5:
      y=1
    elif r<=0.7:
      y=2
    else:
      y=3
    if state[x][y]==0:
      state[x][y]=2
      return state

def score(state):
  score=0
  for x in range(4):
    for y in range(4):
      if state[x][y]==0:
        continue
      score+=int(math.pow(3,math.log(state[x][y],2))*1000)
  return score
