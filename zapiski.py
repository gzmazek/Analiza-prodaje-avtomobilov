import requests

url = "https://www.truecar.com/used-cars-for-sale/listings/bmw/"
odziv = requests.get(url)
with open(f"stran.html", "w") as f:
    f.write(odziv.text)

# https://www.skyscanner.net/transport/flights/vie/aqja/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&rtn=0&qp_prevProvider=ins_browse&qp_prevCurrency=EUR&priceSourceId=&qp_prevPrice=18&oym=2301&selectedoday=01