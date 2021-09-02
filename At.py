""" 
Code for market analysis.

Julio Toboso
"""



# imports


# Analitics Functions
## Running Average
def average( avg, val, n = 1000000):
  avg = (( avg * n ) + val ) / (n + 1) 
  return avg

def overaverage ( ovg, avg, val, n = 1000000):
  if val > avg :
     ovg = (( ovg * n ) + val ) / (n + 1) 
  return ovg

def underaverage ( uvg, avg, val, n = 1000000):
  if val < avg :
     uvg = (( uvg * n ) + val ) / (n + 1) 
  return uvg


