#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 00:54:57 2018

@author: divyanshu
"""

#%%
	
sigma = "ABCD"

def P(c):
	return ord(c) - 65

table = [0]*256
rest = []

def bc1(pat, m):
	for i in range(m):
		table[ord(pat[i])-65] = m-i-1;
	
	rest = str(set(sigma) - set(pat))
	for i in range(len(rest)):
		table[ord(rest[i])-65] = -1;
	#print(rest)
	return table	

def FGS(p):
	gs =[[0 for j in range(26)] for i in range(len(sigma)+1)]
	m = len(p)
	for i in range(len(p)):
		for c in sigma:
			x = ord(c) -  65
			gs[i][x] = len(p) + 1
			
	next = []
	
	for i in range(len(p)):
		next.append(i-1)
		
	for slen in range(len(p)):
		last =  m-1
		i= next[last]
		
		while i>=0:
			if gs[m-slen][P(p[i+1])] > m-1-i:
				if (i-slen < 0 or (i-slen >= 0 and p[i-slen] != p[m-1-slen])):
					gs[m-slen][P(p[i+1])] = m-1-i
					
			if (i-slen >= 0 and p[i-slen] == p[last-slen]) or (i-slen < 0) :
				next[last] = i
				last = i
				
			i = next[i]
			
		if gs[m-slen][P(p[0])] > m:
			gs[m-slen][0] = m
			
		next[last] = -1
	return gs

temp = []
t_ = []
def FFS(p,t):
	n = len(t)
	m = len(p)
	
	for i in range(len(p)+1):
		temp.append(p[m-1])
	
	
	for i in t:
		t_.append(i)
	
	for i in temp:
		t_.append(i)
	
	
	bc = bc1(p.upper(), len(p))	
	gs = FGS(p)
	 
	s = 0
	
	#return t_
	while bc[ord(t_[s+m-1])-65] > 0:
		#print(s+m-1)
		s += bc[ord(t_[s+m-1])-65]
		
	while s<= n-m:
		
		j=m-2
		while j>=0 and p[j] == t_[s+j]:
			j = j-1
			
		#if j<0:
		#	print(s)
			
		s += gs[j+1][ord(t[s+m])-65]
		
		while bc[ord(t_[s+m-1])-65] >0:
			s += bc[ord(t_[s+m-1])-65]
		
	return s


	
def main():
	p = "CACC"
	t = "ABDCACDCACC"
	print( FFS(p, t))
	
	
if __name__=="__main__":
	main()