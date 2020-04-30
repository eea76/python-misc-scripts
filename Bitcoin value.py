#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys, urllib2, json, locale, time

CURRENCY = "USD"

adelle = .28359183
me = .284
clock = time.strftime("%X")
date = time.strftime("%x")

def main():
    asks = []
    bids = []
    
    try:
        url  = "https://data.mtgox.com/api/1/BTC%s/fulldepth" % CURRENCY
        res  = urllib2.urlopen(url, timeout=15)
        data = json.load(res)
        asks = data['return']['asks']
        bids = data['return']['bids']
    except Exception as e:
        print e
        print "ERROR: Unable to fetch fulldepth. Please try again."
        return           

    market_price = float(bids[-1]['price_int']) / 1e5    
    print "Bitcoin price: $%.2f @ MtGox as of %s on %s\n" % (market_price, clock[:-3], date[:-3])
    print "Me: \n%f bitcoins\nWorth $%.2f\n" % (float(me), (me * market_price))
    print "Adelle:\n%f bitcoins\nWorth $%.2f" % (float(adelle), (adelle * market_price))
    

if __name__ == '__main__':
    main()


