import numpy as np
from math import *
import random

n = input("Enter the dimension of the array: ")
#N = input("Enter the number of positions to be changed: ")
f = open("text.txt","w")

#Defining random function
def Random(x,y):
	r = random.randint(x,y)
	return r


#Creating a random vector 
def vector(n):
	a = np.zeros(shape=n)
	for i in range(n):
		a[i] = Random(0,1)
	return a 

#a=vector(n)
 
#print "The vector is :",a

#Defining Weights
def weight(a):
	W = np.zeros(shape=(n,n))
	for j in range(n):
		for i in range(n):	
			W[i,j] = (2*a[j]-1)*(2*a[i]-1)
			if(i==j):
				W[i,j] = 0
	return W

#print "The weight matrix is  = \n", weight(a)

#W = weight(a) 

#-------------O0000----------XXXX------------OOOOO-----------------
N1 = n

for k in range(N1):

	N = k+1

	loop = 0

	count_activated = 0
	count_not_activated = 0

	count_converged = 0
	count_not_converged = 0
#######################################################
	while(loop!=2000):
	
		a=vector(n)
		W = weight(a)
		
		#Taking a random number with probability p = 0.5
		t = random.uniform(1,0)
		
		#Changing the vector with probability p = 0.5
		if (t>=0.5):
		#	print "its changed"	   
			a_new = np.zeros(shape=n)    #Creating a new vector
			
			for i in range(n):
				a_new[i] = a[i]                         
				
		#	print "The unchanged vector is ",a
			
			number = 0
			p = N+1
			while(number!= N):	
				
				h = Random(0,(n-1))   # Changing the position randomly
				if(p!=h):
		#			print "The changed position is: ", h+1
					if (a_new[h]==0):		
						a_new[h] = 1
						number = number+1
					elif (a_new[h]==1):
						a_new[h] = 0
						number = number+1
				p = h
			
		#	print "again the a = ",a
		#	print "The changed vector is   ", a_new	
		
			count_change = 0
			count_not_change = 0	
					
			
			#The condition for checking equality of the vectors	
			condition = np.array_equal(a,(a_new))
		#	print "The condition = ", condition
		
			while(condition==False):
				iteration = 0
				while(iteration!=10000):
			
					l = len(a_new)
					d = Random(0,(n-1))
					x = a_new[d]
					j = d
					v_new = 0
			
					for i in range(l):			
						z = W[i,j] * a_new[i]		
						v_new = v_new + z			
					
					if ((v_new)>=0):
						a_new[j] = 1
						count_change = count_change + 1
					elif ((v_new)<0):
						a_new[j] = 0
						count_not_change = count_not_change + 1
			
					
					condition = np.array_equal(a,a_new)
					iteration = iteration + 1
		
					if(iteration==10000):
		#				print "Did not converge"
						check = 0
		
					if(condition==True):	
						iteration = 10000 
		#				print "It converged"
						check = 1
		
				
				condition = np.array_equal(a,a_new)	
				condition = True
		
				
			if(check==0):
				count_not_converged = count_not_converged + 1
			
			if(check==1):
				count_converged = count_converged + 1  	
				
		#	print "The vector started with is = ",a
		#	print "The converged vector is = ", a_new
		#	print "count_not_converged = ", count_not_converged 
		#	print "count_converged = " , count_converged
			
			count_activated = count_activated + 1 	
			
		loop = loop + 1	
	
		if(t<0.5):
		#	print "its not changed" 
		
			count_not_activated = count_not_activated + 1
	
	
		loop = loop + 1
	
	
	print>>f,N, count_activated,count_not_activated,count_converged,count_not_converged 

#print "\n"
#print "count_activated  = ",count_activated
#print "count_not_activated = ",count_not_activated
#
#print "\n"
#
#print "count_converged = " , count_converged
#print "count_not_converged = ", count_not_converged 


	
#print "\n"
f.close()










