### Heroku-url:
[Oskari running here..](https://oskari.herokuapp.com/ "on heroku")

# Oskari

Oskari on sovellus, joka pitää kirjaa rekisteröityneiden käyttäjien tekemistä osakekaupoista. Käyttäjä voi luoda itselleen salkkuja minne he voivat kirjata tekemiään kauppoja (ostoja sekä myyntejä). Ensin kirjataan osto, jonka jälkeen voidaan kirjata myynti. Jotta sovellus/tietokanta ei paisuisi liian monimutkaiseksi, niin kaupat käsitellään aina kokonaisina eli käyttäjä ei voi myydä osaa osakkeista, vaan tapahtumat käsitellään aina kauppatapahtumana, eli osto- ja myyntimäärät ovat aina yhtä suuria (osakkeitten lkm). Käyttäjälle tai salkulle lasketaan erilaisia yhteenvetoja.

Käyttäjä voi myös kuulua 0..* ryhmään. Samassa ryhmässä olevat voivat tarkastella toistensa salkkuja (sekä niiden tapahtumia?).

CRUD-tauluja ovat siis User, Portfolio sekä Trade, Nämä myös aina liittyvät toisiinsa. Monesta moneen yhteys on tauluilla User ja Group, joka myöskin voi olla CRUD-taulu.

Stock-taulussa on kaikkien tunnettujen yritysten tiedot, nimi sekä kaupankäyntitunnus. Nämä ovat erillisessä taulussa, jotta niitä olisi helppo päivittää tarvittaessa, esim nimi muuttuu tai mahdollisesti lisätä lisää attribuutteja. Jokaiseen kauppaan(Trade) kuuluu aina yksi Stock, mutta Stock voi tietysti kuulua äärettömän moneen Trade:iin. En ole varma kuuluisiko tässä välissä olla (aito) liitostaulu, kyllä kai?

### Tietokantakaavio
[kuva](https://github.com/kordaniel/oskari/tree/master/documentation/db/db_schema.jpg)  
[yuml.me formatoitu dokumentti](https://github.com/kordaniel/oskari/tree/master/documentation/db/db_schema_yuml.txt)

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
  * Poistaa osakkeita järjestelmästä

### Salkku
* Salkku kuuuluu aina tietylle käyttäjälle
* Käyttäjällä voi olla useita sekä hän voi myös poistaa salkkuja
* Salkulla on nimi
* Käyttäjä voi kirjata ostoja
* Käyttäjä voi nähdä mitä osakkeita hän omistaa kyseisenä hetkenä sekä näiden osakkeiden määrän ja ostotapahtuman tiedot salkuittain.
  * Per kauppa
  * Yhteenveto (osakelajeittain)
  * Kauppa ei ole valmis, eli salkussa on tiettyä osaketta kun Trade:n attribuutti sellprice on null/negatiivinen
* Käyttäjä voi myydä (osan) osakkeistaan
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
