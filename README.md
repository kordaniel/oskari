# Oskari
Oskari on sovellus, joka pitää kirjaa rekisteröityneiden käyttäjien tekemistä osakekaupoista. Käyttäjä voi luoda itselleen salkkuja minne he voivat kirjata tekemiään kauppoja (ostoja sekä myyntejä). Ensin kirjataan osto, jonka jälkeen voidaan kirjata myynti. Jotta sovellus/tietokanta ei paisuisi liian monimutkaiseksi, niin kaupat käsitellään aina kokonaisina, eli käyttäjä ei voi myydä osaa kauppaan kuuluvista osakkeista, vaan tapahtumat käsitellään aina kauppatapahtumana, eli osto- ja myyntimäärät ovat aina yhtä suuria (osakkeitten lkm).  

#### CRUD
CRUD-tauluja ovat siis User (account), Portfolio sekä Trade (Muokkaus eli U tulee siitä, kun kirjataan myynti niin päivitetään riville onupdate-aikaleima), Nämä myös aina liittyvät toisiinsa. Monesta moneen yhteys on tauluilla User ja Role. Lisäksi Stock-taulu on myös täysi CRUD-taulu.

Stock-taulussa on kaikkien tunnettujen yritysten tiedot, nimi sekä kaupankäyntitunnus. Nämä ovat erillisessä taulussa, jotta niitä olisi helppo päivittää tarvittaessa, esim nimi muuttuu tai mahdollisesti lisätä lisää attribuutteja. Jokaiseen kauppaan(Trade) kuuluu aina yksi Stock, mutta Stock voi tietysti kuulua äärettömän moneen Trade:iin. En ole varma kuuluisiko tässä välissä olla (aito) liitostaulu, kyllä kai?

### Heroku-url:
[Oskari herokussa](https://oskari.herokuapp.com/)

## Testitunnukset
| Käyttäjätunus | Salasana  | Admin |
|---------------|-----------|-------|
| administrator | topsekret | on    |
| hello         | world     | ei    |
| testi         | testaus   | on    |

## TODO
- Kaikki poisto-operaatiot tapahtuvat välittömästi, tähän pitäisi lisätä vahvistus ennen poistoa.
- Trades-view:iin tarvitaan oikeuksien tarkistamista!
- portfolio.html:ään myös oikeuksien tarkistamista lisättävä!
- Lisättävä notifikaatiot (esim poistojen jälkeen).
- Sekä myöskin virheviestit lisättävä, nyt ohjelma vain ohjaa eri sivuille tilanteesta riippuen, eikä näytä mitään virheviestiä.
- Salkkuun mahdollisuus muuttaa salkun nimeä.
- Riippuen siitä mistä tullaan ja ollaanko ADMIN vai USER, niin ohjausta paranneltava/muutettava jostain kohdista. Nyt toiminta osittain epäloogista.
- Tällä hetkellä sivuilla näytetään datepicker, joka myöskin validoidaan, mutta päivämääriä ei käytetä sovelluslogiikan puolella ollenkaan. HTML5-Datepicker ei myöskään toimi esim. safari-selaimella. Tähän varmaan on kehitettävä jonkunlainen javascript-hässäkkä, joka myöskin tukee kellonaikoja. Chrome ainakin renderöi tuon oikein.


### Asennusohje
[Asennus- sekä käyttöohje](https://github.com/kordaniel/oskari/tree/master/documentation/user_guide.md)  
### Tietokantakaavio
[Tietokantakuvaus](https://github.com/kordaniel/oskari/tree/master/documentation/db/db_description.md)  
Alkuperäiset:  
[kuva](https://github.com/kordaniel/oskari/tree/master/documentation/db/db_schema.jpg)  
[yuml.me formatoitu dokumentti](https://github.com/kordaniel/oskari/tree/master/documentation/db/db_schema_yuml.txt)  

### Käyttäjätarinoita
[Kaikki käyttäjät](https://github.com/kordaniel/oskari/tree/master/documentation/user_stories.md)

## Toimintoja
* Sovellukseen voi lisätä osakkeita, joilla on attribuutit nimi sekä ticker (uniikki lyhenne)

### Käyttäjäprofiilit
* Ylläpitäjä
* Käyttäjä

* Kaikilla on seuraavat attribuutit:
  * Nimi
  * Tunnus
  * Salasana
  * Sähköposti

* Käyttäjät voivat
  * Luoda/poistaa salkkuja
  * Lisätä osakkeita järjestelmään (jos jää aikaa, niin tämä voidaan korvata sopivalla API:lla)
  * Hallita omia tietoja

* Ylläpitäjät voivat
  * Hallita käyttäjiä (muokata sekä poistaa)
  * Muokata osakkeiden tietoja
  * Poistaa osakkeita järjestelmästä

### Salkku
* Salkku kuuuluu aina tietylle käyttäjälle
* Käyttäjällä voi olla useita sekä hän voi myös poistaa salkkuja
* Salkulla on nimi
* Käyttäjä voi kirjata ostoja
* Käyttäjä voi nähdä mitä osakkeita hän omistaa kyseisenä hetkenä sekä näiden osakkeiden määrän ja ostotapahtuman tiedot salkuittain.
  * Per kauppa
  * Yhteenveto (osakelajeittain) - _ei toteutettu, eikä toteuteta tämän kurssin aikana_
  * Kauppa ei ole valmis, eli salkussa on tiettyä osaketta kun Trade:n attribuutti sellprice on null/negatiivinen
* Käyttäjä voi myydä (osan) osakkeistaan - _kaupat käsitellään tällä hetkellä kokonaisina, eli yksittäisiä osakkeita ei voi myydä_
* Kauppa on "valmis", kun osake on myyty, silloin lasketaan tuotto (myynti- ja ostohinnan erotus)

### Kauppatapahtuma koostuu seuraavista tiedoista:
* Osakelaji (yritys)
* Lukumäärä
* Hinta (osto ja myynti)

### Lisäksi ei rekisteröityneet vierailijat voivat:
* Selata osakelistaa
  * ~~Osaketta klikatessa nähdään listan salkuista jotka omistavat kyseistä osaketta~~ KEHITYSEHDOTUS
* ~~Selata anonymisoitua salkkulistaa (listaa kaikista salkuista) sekä avata yksittäisiä salkkuja~~ KEHITYSEHDOTUS

### Mahdollisia lisäominaisuuksia
* Käyttäjä voi tarkastella kauppahistoriaansa, mahdollisesti rajaten sitä tietylle aikavälille
  * Etenkin rajata kalenterivuosittain
* Osakkeille voi lisätä kommentteja, joko niin että kaikki kommentit ovat avoimia kaikille tai sitten tietyille ryhmille tai käyttäjän yksityisiä kommentteja
* Käyttäjä voi piilottaa salkkunsa niin että sitä ei näy missään listassa
* Lisätä eri pörssejä (eri valuutat) joihin yksittäinen osake aina kuuluu
* Osakkeille osingot ja niiden huomioiminen salkuissa
* Käyttäjän kaikkien erillisten salkkujen yhteenveto
* Käyttäjät lisäävät ensin tiedon omiin tietoihinsa, siitä paljonko heillä on toteutuneita tappioita, jolloin sovellus voi laskea tulevien verojen määrää
