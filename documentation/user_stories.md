# Käyttäjätarinoita

## Käyttäjät

### Rekisteröitymätön
#### Voi:  
- Nähdä listauksen kaikista sovelluksen tuntemista osakkeista, aakkosjärjestyksessä. Sivutus käytössä (10 osaketta/sivu).
```
SELECT stock.id AS stock_id, stock.date_created AS stock_date_created, stock.date_modified AS stock_date_modified, stock.ticker AS stock_ticker, stock.name AS stock_name
  FROM stock ORDER BY stock.name
  LIMIT ? OFFSET ?
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
  ```
  DELETE FROM portfolio WHERE portfolio.id = ?
  -Tietokanta poistaa riippuvuudet CASCADE deletellä, jos portfoliolla on riippuvuuksia.
  ```

- Kirjata salkkuihin kauppoja (osto- sekä myyntitapahtuma).
```
Osto:
INSERT INTO trade (date_created, date_modified, portfolio_id, amount, buyprice, sellprice) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
INSERT INTO tradestock (trade_id, stock_id) VALUES (?, ?)
Myynti:
UPDATE trade SET date_modified=CURRENT_TIMESTAMP, sellprice=? WHERE trade.id = ?
```
  - Sekä poistaa näitä yksittäisiä kauppoja.
  ```
  DELETE FROM tradestock WHERE tradestock.trade_id = ? AND tradestock.stock_id = ?
  DELETE FROM trade WHERE trade.id = ?
  ```
- Muokata omia tietoja.
```
UPDATE account SET date_modified=CURRENT_TIMESTAMP, name=?, username=?, email=? WHERE account.id = ?
```
- Poistaa oman tilinsä, jolloin kaikki käyttäjään liitetyt tiedot poistetaan järjestelmästä.
```
DELETE FROM userrole WHERE userrole.user_id = ? AND userrole.role_id = ?
DELETE FROM account WHERE account.id = ?
-jonka lisäksi tietokanta poistaa muut riippuvuudet (portfolio=>..) CASCADE-deletellä, jos niitä muuten jäisi.
```

- User story:  
  "Rekisteröityneenä käyttäjänä haluan mahdollisuuden luoda itselleni erillisiä salkkuja, joihin voin kirjata tekemiäni osakeostoja sekä -myyntejä. Näin voin nähdä mitä osakkeita minulla on tietyssä salkussa tällä hetkellä sekä myös selata näitten historiaa, sisältäen myyntini."

### Ylläpitäjät
- Alkuperäistä käyttäjää (ylläpitäjää, id == 1) ei voi poistaa eikö myöskään poistaa ylläpitäjän roolia tältä.

#### Edellisten lisäksi voi:
- Näkee listan kaikista käyttäjistä järjestelmässä. Sivutus käytössä (5 käyttäjää/sivu).
```
SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.email AS account_email
  FROM account ORDER BY account.name
  LIMIT ? OFFSET ?
```
- Voi asettaa/poistaa ylläpitäjän roolin kaikilta käyttäjilta.
```
Asettaa:
INSERT INTO userrole (user_id, role_id) VALUES (?, ?)
Poistaa:
DELETE FROM userrole WHERE userrole.user_id = ? AND userrole.role_id = ?
```
- Voi muokata minkä tahansa käyttäjän tietoja.
- Voi poistaa minkä tahansa käyttäjän tilin.
```
Katso kohta rekisteröitynyt käyttäjä, samat kyselyt täällä
```

- Muokata osakkeiden tietoja.
```
UPDATE stock SET date_modified=CURRENT_TIMESTAMP, ticker=?, name=? WHERE stock.id = ?
```
- Poistaa osakkeita järjestelmästä, ainoastaan jos osake ei ole liitetty mihinkään kauppatapahtumaan.
```
DELETE FROM stock WHERE stock.id = ?
```
- Näkee listan kaikista salkuista järjestelmässä. Tähän pitää vielä lisätä sivutus..
```
SELECT portfolio.id AS portfolio_id, portfolio.date_created AS portfolio_date_created, portfolio.date_modified AS portfolio_date_modified, portfolio.account_id AS portfolio_account_id, portfolio.name AS portfolio_name
  FROM portfolio ORDER BY portfolio.name
```
- Näkee kaikkien käyttäjien kaikkien salkkujen sisällöt.
- Kirjata kauppoja kaikkiin salkkuihin.
- Poistaa minkä tahansa kaupan.
- Poistaa minkä tahansa salkun.
```
Nämä kyselyt ovat myös samanmuotoisia kuin kohdassa rekisteröitynyt käyttäjä.
```
