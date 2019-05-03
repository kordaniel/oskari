# Asennusohje
Sovelluksen voi ajaa lokaalisti tai herokussa. Toimiakseen sovellus vaatii ympäristöltä python3 sekä pip:in. Testatut tietokannat mitkä toimivat varmasti on sqlite sekä herokun PostgreSQL. Sovelluksen saa helpoiten omaan käyttöön kloonaamalla tämän repositorion git:in avulla. Sovelluksen tarvitsemat moduulit ovat listattuna tiedostossa requirements.txt.

### Sovelluksen ajaminen lokaalisti sekä sen tarvitsemat moduulit
Kun olet kloonannut repositorion, siirry hakemistoon oskari sekä luo sen sisälle virtuaaliympäristö komennolla '_python3 -m venv venv_'. Tämän jälkeen voit ottaa juuri luodun python-virtuaaliympäristön käyttöön suorittamalla komennon '_source venv/bin/activate_'. Seuraavaksi sinun on ladattava ohjelman tarvitsemat moduulit komennolla '_pip install -r requirements.txt_'.  

Nyt voit ajaa sovelluksen komennolla '_python3 run.py_'.  

Lokaalisti ajettuna sovellus luo automaattisesti tarvitsemansa _data.db_ sqlite3-tiedoston hakemistoon _application_, sekä sen jälkeen luo tarvitsemansa tietokantataulut automaattisesti.  

Sovellus myös lisää ylläpitäjän tunnuksen, jolla on tunnus/salasanapari: _admininstrator/topsekret_.  


### Sovelluksen ajaminen herokussa
Sovelluksen mukana tulee tiedosto '_Procfile_', johon on määritelty herokun tarvitsemat komennot sovelluksen ajamiseen. Sovelluksen mukana tulee myös tiedosto '_requirements_', joka sisältää listauksen kaikista sovelluksen tarvitsemista moduuleista. Heroku lataa kaikki moduulit automaattisesti sekä tarjoaa tarvittavan PostgreSQL-tietokannan.  

Sovellus luo tarvitsemansa tietokantataulut sekä ylläpitäjän käyttäjätunnuksen automaattisesti, ylläpitäjän luontia varten sovellus tarvitsee seuraavat ympäristömuuttujat:  
```
SU_NAME - pääkäyttäjän koko nimi  
SU_USERNAME - pääkäyttäjän käyttäjätunnus  
SU_PASSWD - pääkäyttäjän salasana  
SU_EMAIL - pääkäyttäjän sähköpostiosoite  
```

Sovellus asennetaan herokuun käyttämällä heroku toolbeltiä, joka on oltava asennettuna paikalliselle koneelle. Jos ajat kaikki komennot, niin muuta konfiguraatiota ei tarvitse tehdä. Kaiken pystyy todennäköisesti myös tekemään herokun nettisivujen kautta, mutta suosittelen allaolevia komentoja niiden yksinkertaisuuden vuoksi. Komennot on ajettava kloonatun repositorion juuressa:  

```
heroku create <valitsemasi-nimi>  
heroku config:set SU_NAME="<koko nimi>"  
heroku config:set SU_USERNAME="<ylläpitäjän_tunnus>"  
heroku config:set SU_PASSWD="<ylläpitäjän salasana>"  
heroku config:set SU_EMAIL="<ylläpitäjän sposti>"  
git remote add heroku <https://git.heroku.com/...>, missä ... on herokun palauttama osoite.  
tarvittaessa git add . sekä git commit -m "lähetys herokuun"  
git push heroku master  
```  

Jos haluat tyhjentää tietokannan jostain syystä, niin aja seuraavat komennot kloonatun repositorion juuressa:  

```
heroku pg:reset DATABASE
<vastaa kysymyksiin>
heroku reset
```

# Käyttöohje
Kun sovellus ajetaan ensimmäisen kerran niin se siis luo automaattisesti ylläpitäjän roolilla varustetun käyttäjän. Tätä käyttäjää ei pysty poistamaan, eikä siltä myöskään voi poista ylläpitäjän roolia. Muutoin ylläpitäjän profiilia voi muokata kuten myös kaikkia muitakin. Suosittelen ainakin salasanan vaihtoa! :)  

Tulevat käyttäjät voivat rekisteröityä etusivun linkin kautta, jolloin sovellusta voi ruveta käyttämään. Ylläpitäjän roolin omaavat käyttäjät, eli alussa vain administrator-käyttäjä voi asettaa sekä poistaa kaikilta käyttäjiltä ylläpitäjän roolin. Tämä tapahtuu Users-sivulta, joka näkyy vain ylläpitäjille. Ylläpitäjät voivat myös poistaa käyttäjiä samalta sivulta.  

Käyttäjät voivat luoda itselleen salkkuja linkistä add portfolio. Tämän jälkeen käyttäjät voivat kirjata ostotapahtumia salkkuihinsa (Add position). Jotta lisäys onnistuisi, on järjestelmässä ensin oltava kyseinen osake, jonka voi lisätä linkistä Add stock. Kun salkussa sitten on ostotapahtumia, niin ne voidaan sulkea, joka vastaa osakkeen myymistä (Close position).
