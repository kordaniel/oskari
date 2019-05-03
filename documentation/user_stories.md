# Käyttäjätarinoita

## Käyttäjät

### Rekisteröitymätön
#### Voi:  
- Nähdä listauksen kaikista sovelluksen tuntemista osakkeista, aakkosjärjestyksessä. Sivutus käytössä (10 osaketta/sivu).
```
SELECT stock.id AS stock_id, stock.date_created AS stock_date_created, stock.date_modified AS stock_date_modified, stock.ticker AS stock_ticker, stock.name AS stock_name
  FROM stock ORDER BY stock.name
```
- Rekisteröityä järjestelmään.
```
INSERT INTO account (date_created, date_modified, name, username, password, email) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

### Rekisteröitynyt käyttäjä
#### Edellisen lisäksi voi:
- Lisätä osakkeita järjestelmään
```
INSERT INTO stock (date_created, date_modified, ticker, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
```
- Luoda itselleen salkkuja.
   ```
   INSERT INTO portfolio (date_created, date_modified, account_id, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
   ```
  - Sekä poistaa omia salkkuja (kauppoineen kaikkineen).
- Kirjata salkkuihin kauppoja (osto- sekä myyntitapahtuma).
  - Sekä poistaa näitä yksittäisiä kauppoja.
- Muokata omia tietoja.
- Poistaa oman tilinsä, jolloin kaikki käyttäjään liitetyt tiedot poistetaan järjestelmästä.

- User story:  
  "Rekisteröityneenä käyttäjänä haluan mahdollisuuden luoda itselleni erillisiä salkkuja, joihin voin kirjata tekemiäni osakeostoja sekä -myyntejä. Näin voin nähdä mitä osakkeita minulla on tietyssä salkussa tällä hetkellä sekä myös selata näitten historiaa, sisältäen myyntini."

### Ylläpitäjät
- Alkuperäistä käyttäjää (ylläpitäjää, id == 1) ei voi poistaa eikö myöskään poistaa ylläpitäjän roolia tältä.

#### Edellisten lisäksi voi:
- Näkee listan kaikista käyttäjistä järjestelmässä. Sivutus käytössä (5 käyttäjää/sivu).
- Voi asettaa/poistaa ylläpitäjän roolin kaikilta käyttäjilta.
- Voi muokata minkä tahansa käyttäjän tietoja.
- Voi poistaa minkä tahansa käyttäjän tilin.

- Muokata osakkeiden tietoja.
- Poistaa osakkeita järjestelmästä, ainoastaan jos osake ei ole liitetty mihinkään kauppatapahtumaan.

- Näkee listan kaikista salkuista järjestelmässä. Tähän pitää vielä lisätä sivutus..
- Näkee kaikkien käyttäjien kaikkien salkkujen sisällöt.
- Kirjata kauppoja kaikkiin salkkuihin.
- Poistaa minkä tahansa kaupan.
- Poistaa minkä tahansa salkun.
