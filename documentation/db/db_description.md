# Tietokanta
![Tietokantakuvaus](https://raw.githubusercontent.com/kordaniel/oskari/tree/master/documentation/db/db_schema_vko6.jpg)  

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
        FOREIGN KEY(user_id) REFERENCES account (id),
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
        FOREIGN KEY(account_id) REFERENCES account (id)
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
        FOREIGN KEY(portfolio_id) REFERENCES portfolio (id)
)

CREATE TABLE tradestock (
        trade_id INTEGER NOT NULL,
        stock_id INTEGER NOT NULL,
        PRIMARY KEY (trade_id, stock_id),
        FOREIGN KEY(trade_id) REFERENCES trade (id),
        FOREIGN KEY(stock_id) REFERENCES stock (id)
)
```  
