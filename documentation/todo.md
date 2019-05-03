# Going forward

## TODO
- Yleistää koodia, nyt tehdään samaa asia monta kertaa eri funktioissa, esim view:eissa kun tarkistetaan käyttäjän oikeuksia, Modeleihin lisätä abstrakti model, jolla on kenttä nimi sekä vuorostaan extendaa Basen.
- Kaikki poisto-operaatiot tapahtuvat välittömästi, tähän pitäisi lisätä vahvistus ennen poistoa.
- Trades-view:iin tarvitaan oikeuksien tarkistamista!
- portfolio.html:ään myös oikeuksien tarkistamista lisättävä!
- Lisättävä notifikaatiot (esim poistojen jälkeen).
- Sekä myöskin virheviestit lisättävä, nyt ohjelma vain ohjaa eri sivuille tilanteesta riippuen, eikä näytä mitään virheviestiä.
- Salkkuun mahdollisuus muuttaa salkun nimeä.
- Riippuen siitä mistä tullaan ja ollaanko ADMIN vai USER, niin ohjausta paranneltava/muutettava jostain kohdista. Nyt toiminta osittain epäloogista, esim ylläpitäjän roolilla käyttäjien salkuissa oleva back to profile-linkki.
- Tällä hetkellä sivuilla näytetään datepicker, joka myöskin validoidaan, mutta päivämääriä ei käytetä sovelluslogiikan puolella ollenkaan. HTML5-Datepicker ei myöskään toimi esim. safari-selaimella. Tähän varmaan on kehitettävä jonkunlainen javascript-hässäkkä, joka myöskin tukee kellonaikoja. Chrome ainakin renderöi tuon oikein.
