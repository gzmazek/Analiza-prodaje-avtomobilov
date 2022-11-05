import requests
import time

MAKSIMALNA_STRAN = 923
CAS_MED_ZAJEMANJEM = 0
# https://www.truecar.com/used-cars-for-sale/listings/?page=900

for i in range(1, MAKSIMALNA_STRAN):
    time.sleep(CAS_MED_ZAJEMANJEM)
    url = f"https://www.truecar.com/used-cars-for-sale/listings/bmw/?page={i}"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        print(url)
        with open(f"cars_data_2/bmw_page_{i}.html", "w") as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")