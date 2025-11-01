# Product Category Classifier

## Automatska klasifikacija proizvoda po kategorijama pomoću mašinskog učenja.

## Instalacija
### Pokreni instalaciju potrebnih paketa:

``` bash
pip install -r requirements.txt
```
## Pokretanje
### Treniranje modela
`Pokreni skriptu za treniranje modela:`

``` bash
python scripts/train_model.py
```
## Ovo će sačuvati model u model/product_classifier.pkl.

## Predikcija nove kategorije
`Pokreni skriptu za automatsku klasifikaciju proizvoda:`
``` bash
python scripts/predict_category.py
```

### Uneti naziv proizvoda kada bude zatraženo, npr.:
`iphone 7 32gb gold`


### Izlaz će biti predviđena kategorija, npr.:
`Predviđena kategorija: Mobile Phones`


### Za izlazak iz skripte, ukucaj:
`exit`


## Primeri:

| Naziv proizvoda         | Kategorija        |
|--------------------------|------------------|
| iphone 7 32gb gold       | Mobile Phones    |
| olympus e m10 mark iii   | Digital Cameras  |
| bosch serie 4 kgv39vl31g | Fridge Freezers  |