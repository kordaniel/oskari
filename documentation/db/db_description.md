# Tietokanta
![Tietokantakuvaus](https://raw.githubusercontent.com/kordaniel/oskari/master/documentation/db/db_schema_vko6.jpg)  

Sovellus on suunniteltu niin, että se käyttää hyväkseen tietokannan tarjoamaa CASCADE deleteä. Kuten CREATE TABLE-lauseista voi lukea, niin Role, Account sekä Stock -tauluilla ei ole tätä käytössä. Näin ollen jos halutaan poistaa jokin rivi näistä tauluista, niin se täytyy tehdä erikseen. Tarkoitus onkin, että näin tulisi toimia. Rooleja on tällä hetkellä vain kaksi, eikä niitä voi lisätä/muutella mistään. Käyttäjiä ja Osakkeita ei tietenkään tule poistaa muutoin kuin käyttöliittymän kautta.

Nyt koska Tradestockilla on viiteavain Traden pääavaimeen sekä myös ON DELETE CASCADE määriteltynä, niin jos Trade poistetaan, niin tietokanta poistaa myös Tradestockin rivit jotka liittyvät poistettavaan Trade-riviin ja Stock-taulun rivi jää järjestelmään. Vastaavasti koska Trade:iin on määritelty ON DELETE CASCADE viiteavain Portfolio:n pääavaimeen, niin Portfolio-rivin poistaminen poistaa kaikki siihen kuuluvat Trade-rivit.

Aivan vastaavasti on myös määritelty tauluille Portfolio sekä Userrole ON DELETE CASCADE-viiteavaimet taululle Account.  

Näin ollen voidaan aina olla varmoja siitä, että mistä tahansa taulusta poistettaessa, niin mihinkään tauluun ei jää "orpoja" rivejä. Tietokannassa siis on tietynlainen "järjestys", hierarkia. Jos poistetaan käyttäjä, niin poistetaan myös kaikki käyttäjään liittyvät rivit kaikista tauluista sekä myös jatketaan poistamista hierarkiassa aina alaspäin, aina tauluihin Userrole sekä Tradestock:iin asti.  

Vastaavasti jos poistetaan rivi jostain taulusta, mikä on "alempana" hierarkiassa, esim. Trade, niin poistetaan Trade-rivi sekä kaikki siihen kuuluvat rivit hierarkiassa alempana olevista tauluista, mutta ei hierarkiassa ylempänä olevista tauluista.  

Koska sovellus luottaa siihen, että tietokanta poistaa riippuvuudet ON DELETE CASCADE:n avulla, kuten myös muutenkin on varmaan järkevää, niin tietokannan täytyy totella viiteavaimien rajoitteita. Herokun PostgreSQL:ässä tämä on automaattisesti käytössä. Lokaalisti ajettaessa on sqlite3-tietokannalle määriteltävä:  
```
PRAGMA foreign_keys = ON;
```  
Sovellus myös asettaa tämän rajoitteen automaattisesti käyttöön luodessaan tietokannan, joten käyttäjän ei itse tarvitse tästä huolehtia.

### Kehitysehdotuksia  
Vaikka tällä hetkellä (pää- tai viiteavaimia) ei muutella, niin varmaan olisi syytä ottaa käyttöön ON UPDATE CASCADE-määreet myös, jotta voitaisiin aina olla varmoja tietokannan eheydestä. Toinen muutos mitä tulen miettimään, on Tradestock-liitostaulun poistaminen ja määritellä Trade:iin kuuluva Stock:in pääavain suoraan Tradeen viiteavaimeksi. Tästä en kyllä ole varma mikä on oikea ratkaisu, kyseessähän on monen suhde yhteen-yhteys (kauppa koskee aina vain yhtä osaketta, mutta osake voi tietysti kuulua äärettömän moneen kauppaan), mutta toisaalta Trade:ssa on niin monta attribuuttia. Kurssin alkupuolella kävin pajassa, ja silloin neuvottiin käyttämään liitostaulua, joten olen nyt päätynyt tähän ratkaisuun.  

### Monimutkaisemmat yhteenvetokyselyt
Sovelluksessa on monimutkaisempi tietokantakysely joka kohdistuu tauluihin Trade, Tradestock ja Stock. Nämä on määritelty portfolio:n modeliin:

### Portfolio-sivulla näytettävät avoimet kaupat
```
SELECT Stock.ticker, Stock.name, Trade.id, Trade.date_created AS buydate,  Trade.amount, Trade.buyprice
    FROM Trade, Tradestock, Stock
    WHERE Trade.portfolio_id = :portfolio_id
    AND Trade.sellprice IS null
    AND Trade.id = Tradestock.trade_id
    AND Tradestock.stock_id = Stock.id;
```
### Sekä suljetut/valmiit kaupat:
#### PostgreSQL:ässä käytettävä lause:
```
SELECT Stock.ticker, Stock.name, Trade.date_created AS buydate,
        Trade.date_modified AS selldate, Trade.amount, Trade.buyprice, Trade.sellprice,
        ROUND(((Trade.sellprice - Trade.buyprice) * Trade.amount)::numeric, 2) AS total_return
    FROM Trade, Tradestock, Stock
    WHERE Trade.portfolio_id = :portfolio_id
    AND Trade.sellprice IS NOT null
    AND Trade.id = Tradestock.trade_id
    AND Tradestock.stock_id = Stock.id
```
#### Sqlite3:n vastaava:
```
SELECT Stock.ticker, Stock.name,
        Trade.date_created AS buydate, Trade.date_modified AS selldate, Trade.amount,
        Trade.buyprice, Trade.sellprice,
        ROUND(((Trade.sellprice - Trade.buyprice) * Trade.amount), 2) AS total_return
    FROM Trade, Tradestock, Stock
    WHERE Trade.portfolio_id = :portfolio_id
    AND Trade.sellprice IS NOT null
    AND Trade.id = Tradestock.trade_id
    AND Tradestock.stock_id = Stock.id
```

### Create table lauseet
```
CREATE TABLE role (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(16) NOT NULL,
        superuser BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (name),
        CHECK (superuser IN (0, 1))
)

CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(80) NOT NULL,
        password VARCHAR(80) NOT NULL,
        email VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username),
        UNIQUE (email)
)

CREATE TABLE userrole (
        user_id INTEGER,
        role_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES account (id) ON DELETE CASCADE,
        FOREIGN KEY(role_id) REFERENCES role (id)
)

CREATE TABLE stock (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        ticker VARCHAR(16) NOT NULL,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (ticker)
)

CREATE TABLE portfolio (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        account_id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
)

CREATE TABLE trade (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        portfolio_id INTEGER NOT NULL,
        amount INTEGER NOT NULL,
        buyprice FLOAT NOT NULL,
        sellprice FLOAT,
        PRIMARY KEY (id),
        FOREIGN KEY(portfolio_id) REFERENCES portfolio (id) ON DELETE CASCADE
)

CREATE TABLE tradestock (
        trade_id INTEGER,
        stock_id INTEGER,
        FOREIGN KEY(trade_id) REFERENCES trade (id) ON DELETE CASCADE,
        FOREIGN KEY(stock_id) REFERENCES stock (id)
)
```  
