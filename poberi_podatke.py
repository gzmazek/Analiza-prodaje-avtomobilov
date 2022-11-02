import requests
import time

for i in range(1, 5):
    time.sleep(5)
    url = f"https://www.truecar.com/used-cars-for-sale/listings/?page={i}"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        print(url)
        with open(f"cars_data/cars_data_page_{i}.html", "w") as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")

# https://www.truecar.com/used-cars-for-sale/listings/?page=900