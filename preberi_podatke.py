import re

vzorec_bloka = re.compile(
    r'<li\sclass="mt(?P<blok>.+?)'
    r'</div>\s*</li>',
    flags=re.DOTALL
)

vzorec_oglasa = re.compile(
    r'<a\shref="/used-cars-for-sale/listing/(?P<vse>.*?)/".*'
#    r'aria-label=(?P<naslov>)data-test="usedListing"'
    r'data-test="vehicleCardPricingBlockPrice">(?P<price>.*?)</div>.*'
    r'</circle>\s*</svg>(?P<miles>.*?)<!--\s-->\smiles</div>.*'
    r'</path></svg>(?P<city>.*?)<!--\s-->,\s<!--\s-->(?P<state>.*?)</div><div\sclass="vehicle-card-location.*'
    r'</svg>(?P<exterior>.*?)<!--\s-->\sexterior.*'
    r'-->(?P<interior>.*?)<!--\s-->\sinterior</div></div><div.*'
    r'</path></svg>(?P<accidents>.*?)\saccidents?,\s(?P<owners>.*?)\sOwners?,\s(?P<use>.*?)\suse</div>.*'
    r'ill-rule="evenodd"></path></svg>(?P<podatki>.*?)</div><div\sclass="vehicle-card.*',
    flags=re.DOTALL
)


count = 0
for i in range(1, 920):
    with open(f"cars_data_2/bmw_page_{i}.html") as f:
        vsebina = f.read()
    for blok in vzorec_bloka.finditer(vsebina):
        try:
#            print(blok.group(0)[-1000:])
            print(vzorec_oglasa.search(blok.group(0)).groupdict())
            count += 1
            print(count, i)
        except:
            pass

print(count)

#    r'</path></svg>(?P<MPG>.*?)Engine:\s(?P<engine>.*?),\sTransmission:\s(?P<transmission>.*?)</div>.*'
#    r'</path></svg>(?P<general>.*?)</div><div\s
#    r'class="vehicle-card-vin-carousel\stext-xs">VIN:\s<!--\s-->(?P<VIN>.*?)</div></div></div></div></li><li.*'


