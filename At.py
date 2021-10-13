""" 
Code for market analysis.

Julio Toboso
"""
# virtual env
mkvirtualenv -p $(which python3) bitcoin_notifications
workon bitcoin_notifications  # To activate the virtual environment

#installs
pip install requests==2.18.4  # We only need the requests package


# imports
import math
from time
#from binance.websockets import BinanceSocketManager
#from binance.client import Client

import requests




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
def freqverage_complex ( f, fvgRe, fvgIm, val, n = int(time.time() ) ):
  print(n)
  fvgRe = fvgRe + val * cos ( 2 * pi * f * n )
  fvgIm = fvgIm + val * sin ( -2 * pi * f * n )
  return fvgRe, fvgIm
  
def fourier ( T, fvgRe, fvgIm, val, n = int(datetime.now()) ):
  Re, Im = freqverage_complex ( 1/T, fvgRe, fvgIm, val)
  Mod = sqrt ( Re**2 + Im**2 )
  atn = atan( Im / Re) 
  cuadrant = atn * 4 / pi
  Delay = atn * T / (2 * pi)
  return Mod, Delay, cuadrant

#def FreqAnalysis 



BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])

