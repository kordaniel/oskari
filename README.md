# Oskari

Oskari on sovellus, joka pitää kirjaa rekisteröityneiden käyttäjien tekemistä osakekaupoista. Käyttäjillä on aina vähintään yksi salkku, minne he voivat kirjata tekemiään kauppoja (ostoja sekä myyntejä). Käyttäjä voi ainoastaan kirjata myyntejä sellaisista osakkeista joita hän omistaa. Käyttäjällä voi olla useita salkkuja. Käyttäjälle lasketaan erilaisia yhteenvetoja. Aluksi 


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
  * Hallita käyttäjiä
  * Poistaa osakkeita järjestelmästä

### Salkku
* Salkku kuuuluu aina tietylle käyttäjälle
* Käyttäjällä voi olla useita sekä voi myös poistaa salkkuja
* Salkulle voi antaa nimen
* Käyttäjä voi kirjata ostoja
* Käyttäjä voi nähdä mitä osakkeita hän omistaa kyseisenä hetkenä sekä näiden osakkeiden määrän ja ostotapahtuman tiedot salkuittain.
  * Per kauppa
  * Yhteenveto (osakelajeittain)
* Käyttäjä voi myydä (osan) osakkeistaan
* Käyttäjä voi tarkastella kauppahistoriaansa
* Kauppa on "valmis", kun osake on myyty, silloin lasketaan tuotto (myynti- ja ostohinnan erotus)
* Käyttäjä voi rajata tapahtumia tietylle aikavälille
  * Etenkin nähdä kalenterivuoden ajanjakson tuloksen(voitto/tappio)

### Kauppatapahtuma koostuu seuraavista tiedoista:
* Osakelaji (yritys)
* Lukumäärä
* Aika
* Osto vai myynti

### Lisäksi ei rekisteröityneet vierailijat voivat:
* Selata osakelistaa
  * Osaketta klikatessa nähdään lista salkuista jotka omistavat kyseistä osaketta
* Selata anonymisoitua salkkulistaa (listaa kaikista salkuista) sekä avata yksittäisiä salkkuja

### Mahdollisia lisäominaisuuksia
* Käyttäjät voivat muodostaa suljettua ryhmiä. Tällöin he voisivat nähdä kaikki tiedot toistensa salkuista. Voisivat myös käydä keskusteluja keskenään.
* Osakkeille voi lisätä kommentteja, joko niin että kaikki kommentit ovat avoimia kaikille tai sitten tietyille ryhmille tai käyttäjän yksityisiä kommentteja
* Käyttäjä voi piilottaa salkkunsa niin että sitä ei näy missään listassa
* Lisätä eri pörssejä (eri valuutat) joihin yksittäinen osake aina kuuluu
* Osakkeille osingot ja niiden huomioiminen salkuissa
* Käyttäjän kaikkien erillisten salkkujen yhteenveto
* Käyttäjät lisäävät ensin tiedon omiin tietoihinsa, paljonko heillä on toteutuneita tappioita, jolloin sovellus voi laskea tulevien verojen määrää
