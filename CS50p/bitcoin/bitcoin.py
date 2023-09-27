### Bitcoin API lab
import sys
import requests
import json

#request and fetch API
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    coinprice=r.json()
    rate = float(coinprice['bpi']['USD']['rate_float'])
except requests.RequestException:
    pass

##main code to input system argument and check for ValueError
def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        try:
            f = float(sys.argv[1])
        except(ValueError):
            sys.exit("Command-line argument is not a number")
    o = rate*float(sys.argv[1])
###print 4 decimal points
    print(f"${o:,.4f}")





main()