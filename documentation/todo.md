# Going forward

## TODO
- Muuttaa salasanan tallenusta, selväkielisestä tiivisteeseen, esim bcryptin avulla.
- Yleistää koodia, nyt tehdään samaa asia monta kertaa eri funktioissa, esim view:eissa kun tarkistetaan käyttäjän oikeuksia, Modeleihin lisätä abstrakti model, jolla on kenttä nimi sekä vuorostaan extendaa Basen.
- Kaikki poisto-operaatiot tapahtuvat välittömästi, tähän pitäisi lisätä vahvistus ennen poistoa.
- Trades-view:iin tarvitaan oikeuksien tarkistamista!
- portfolio.html:ään myös oikeuksien tarkistamista lisättävä!
- Lisättävä notifikaatiot (esim poistojen jälkeen).
- Sekä myöskin virheviestit lisättävä, nyt ohjelma vain ohjaa eri sivuille tilanteesta riippuen, eikä näytä mitään virheviestiä.
- Salkkuun mahdollisuus muuttaa salkun nimeä.
- Riippuen siitä mistä tullaan ja ollaanko ADMIN vai USER, niin ohjausta paranneltava/muutettava jostain kohdista. Nyt toiminta osittain epäloogista, esim ylläpitäjän roolilla käyttäjien salkuissa oleva back to profile-linkki.
- Tällä hetkellä sivuilla näytetään datepicker, joka myöskin validoidaan, mutta päivämääriä ei käytetä sovelluslogiikan puolella ollenkaan. HTML5-Datepicker ei myöskään toimi esim. safari-selaimella. Tähän varmaan on kehitettävä jonkunlainen javascript-hässäkkä, joka myöskin tukee kellonaikoja. Chrome ainakin renderöi tuon oikein.

## Ajatuksia
- Tällä hetkellä melkein kaikki tieto haetaan suoraan tietokannasta jokaisen sivunlatauksen yhteydessä. Kyselyjä tulee siis valtavasti, kun itse operaation lisäksi tarkistetaan mm. käyttäjien oikeuksia. Tätä helpottamaan voisi varmaan esim. Userin modelliin tallentaa tietoja, joita sitten päivitettäisiin tietyn ajan kuluttua tai silloin kun tietokannassa tapahtuu muutoksia. Tai todennäköisesti on olemassa fiksumpia ratkaisuja, pitää yrittää tutustua asiaan.
- Suurin osa kyselyistä tapahtuu flask SQLAlchemyn tekemänä, ja näin ollen tietokannasta haetaan usein paljon sellaista tietoa, mitä ei kyseiseen operaatioon aina tarvita. Tähän varmaan SQLAlchemy tarjoaa ratkaisuja tai sitten pitäisi itse kirjoittaa sopivat SQL-kyselyt helpottamaan tietokannan työtä.
