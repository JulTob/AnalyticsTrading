""" 
Code for market analysis.

Julio Toboso
"""



# imports
import math
from datetime import datetime



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

def trendverage ( tvg, avg, val,  n = 1000000):
  tvg = ( ( tvg * n ) + ( val - avg ) ) / (n+1)
  return tvg

pi = math.pi
def freqverage ( f, fvgRe, fvgIm, val, n = int(datetime.now()) ):
  print(n)
  fvgRe = fvgRe + val * cos ( 2 * pi * f * n )
  fvgIm = fvgIm + val * sin ( -2 * pi * f * n )
  return fvgRe, fvgIm
  
