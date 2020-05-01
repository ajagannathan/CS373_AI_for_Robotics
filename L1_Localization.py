#Modify the previous code so that the robot senses red twice.

p=[0.2, 0.2, 0.2, 0.2, 0.2]							#Uniform pior probability distribution of where the robot might be
world=['green', 'red', 'red', 'green', 'green']				#The world the robot is in
measurements = ['red', 'red']								#The measurements of the robot i.e data collected of the world
motions = [1,1]												#amount by which the robot moves

pHit = 0.6													#probability of the measurement being a hit or miss
pMiss = 0.2

pExact = 0.8												#probability that the robot moved exactly, overshot or undershot
pOvershoot = 0.1
pUndershoot = 0.1

#This function returns the normalized posterior probability distribution
#based on the measurements taken by the robot
#The output is normalized so that the probabilities sum up to 1
def sense(p, Z):											
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

#This function returns the posterior probability distribution
#based on the robots inexact motion.
def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
	
#Performing a sense and a move multiple times 
#we can find out the probability of where the robot 
#might be in the world
#In other words we have localized the robot
for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])
    
print (p)       
