# Asennusohje
Sovelluksen voi ajaa lokaalisti tai herokussa. Toimiakseen sovellus vaatii ympäristöltä python3 sekä pip:in. Testatut tietokannat mitkä toimivat varmasti on sqlite sekä herokun PostgreSQL. Sovelluksen saa helpoiten omaan käyttöön kloonaamalla tämän repositorion git:in avulla. Sovelluksen tarvitsemat moduulit ovat listattuna tiedostossa requirements.txt.

### Sovelluksen ajaminen lokaalisti sekä sen tarvitsemat moduulit
Kun olet kloonannut repositorion, siirry hakemistoon oskari sekä luo sen sisälle virtuaaliympäristö komennolla _python3 -m venv venv_. Tämän jälkeen voit ottaa juuri luodun python-virtuaaliympäristön käyttöön komennolla _source venv/bin/activate_. Seuraavaksi sinun on ladattava ohjelman tarvitsemat moduulit komennolla _pip install -r requirements.txt_.  

Nyt voit ajaa sovelluksen komennolla _python3 run.py_.  

Lokaalisti ajettuna sovellus luo automaattisesti tarvitsemansa data.db sqlite3 tiedoston hakemistoon application.


### Sovelluksen ajaminen herokussa
Sovelluksen mukana tulee tiedosto Procfile, jossa on määritelty herokun tarvitsemat komennot sovelluksen ajamiseen. Heroku lataa kaikki moduulit automaattisesti ja tarjoaa tarvittavan PostgreSQL-tietokannan.  

Asennus herokuun menee ihan normaalisti, ilman sen suurempia konfiguraatioita, komennot oskari-hakemistossa:  
heroku create <valitsemasi-nimi>  
git remote add heroku <https://git.heroku.com/...>, missä ... on herokun palauttama osoite.  
tarvittaessa git add . sekä git commit -m "lähetys herokuun"  
git push heroku master  

# Käyttöohje
Kun sovellus ajetaan ensimmäisen kerran niin se luo automaattisesti ylläpitäjän roolilla varustetun käyttäjän administrator, jolla on salasana topsekret. Tätä käyttäjää ei pysty poistamaan, eikä myöskään poistamaan ylläpitäjän roolia. Tulevat käyttäjät voivat rekisteröityä etusivun linkin kautta, jolloin sovellusta voi ruveta käyttämään. Ylläpitäjän roolin omaavat käyttäjät, eli alussa vain administrator-käyttäjä voi asettaa sekä poistaa kaikilta käyttäjiltä ylläpitäjän roolin. Tämä tapahtuu Users-sivulta joka näkyy vain ylläpitäjille. Ylläpitäjät voivat myös poistaa käyttäjiä samalta sivulta.  

Käyttäjät voivat luoda itselleen salkkuja linkistä add portfolio. Tämän jälkeen käyttäjät voivat kirjata ostotapahtumia salkkuihinsa (Add position). Jotta lisäys onnistuisi, on järjestelmässä ensin oltava kyseinen osake, jonka voi lisätä linkistä Add stock. Kun salkussa sitten on ostotapahtumia, niin ne voidaan sulkea, joka vastaa osakkeen myymistä (Close position).