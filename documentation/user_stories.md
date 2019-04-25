# Käyttäjätarinoita

## Käyttäjät

### Ylläpitäjät
Voi muokata tai poistaa käyttäjiä. Voi poistaa osakkeita järjestelmästä.
Vko6 tila: Nämä on toteutettu. Tosin bugeja löytyy vielä: jos käyttäjä on luonut salkun, niin käyttäjää ei pysty poistamaan.

### Rekisteröitymätön
Voi nähdä listauksen kaikista sovelluksen tuntemista osakkeista.
Vko6 tila: toteutettu ja toimii

### Rekisteröitynyt käyttäjä
Rekisteröityneenä käyttäjänä haluan mahdollisuuden luoda itselleni erillisiä salkkuja, joihin voin kirjata tekemiäni osakeostoja sekä -myyntejä. Näin voin nähdä mitä osakkeita minulla on tietyssä salkussa tällä hetkellä sekä myös selata näitten historiaa, sisältäen myyntini. Haluan myös mahdollisuuden nähdä kaikkien eri salkuissani olevieni osakkeitten yhteenvedon.

Haluan myös mahdollisuuden perustaa ryhmiä johon muut käyttäjät voisivat mahdollisesti liittyä ja ryhmän sisällä voitaisiin nähdä muiden ryhmään kuuluvien salkut/tiedot.

vko6 tila:
Rekisteröity käyttäjä voi luoda itselleen salkkuja sekä kirjata kauppoja niihin. Ryhmiä en toteuta, mutta olen tehnyt erillisen Role-taulun johon tallennetaan eri mahdolliset roolit johon käyttäjä voi kuulua. Kaikki käyttäjät kuuluvat ryhmään USER ja ylläpitäjät kuuluvat myös ryhmään ADMIN. Tässä on siis monen suhde moneen yhteys. Salkun näyttävä sivu ei ole kovin käyttäjäystävällinen tällä hetkellä, formi pitää muotoilla uudestaan vielä.
