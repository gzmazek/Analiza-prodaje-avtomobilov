# Analiza prodaje avtomobilov

Repozitorij za domačo nalogo pri predmetu *Programiranje 1* v 2. letniku programa *Matematika* na *Fakulteti za matematiko in fiziko Univerze v Ljubljani*.

---

# Zbiranje podatkov

Podatke bom zbiral iz [Spletne strani Truecar](https://www.truecar.com) o cenah trenutnih avtomobilov na trgu v ZDA. Pri vsakem oglasu bom zajel znamko avtomobila, model avtomobila, leto proizvodnje, ceno avtomobila, lokacijo (mesto in zvezna država), porabo, barvo notranjosti in zunanjosti avtomobila, število lastnikov avtomobila, število nesreč, v katerih je bil avtomobil, in karakteristike motorja avtomobila.

---

# Obdelava podatkov

S pridobljenimi podatki želim ugotoviti:
- kakšno je razmerje med starostjo avtomobila in ceno,
- ali starost avtomobila vpliva eksponentno na ceno,
- kateri podatki so odvisni med seboj in kateri neodvisno vplivajo na ceno,
- ali so avtomobili z avtomatičnim menjalnikom povprečno dražji?

---

# Nameščanje dodatnih knjižnic

V obdelavi podatkov sem uporabil knjižnico seaborn, ki jo namestite z ukazom `pip install seaborn` ali `pip3 install seaborn`

