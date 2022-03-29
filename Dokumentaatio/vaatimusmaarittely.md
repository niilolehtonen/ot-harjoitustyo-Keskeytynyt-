# Vaatimusmäärittely
## Sovelluksen idea
Sovelluksen käyttäjä voi valita spotify kirjastostaan soittolistan, jonka avulla käyttäjälle luodaan uusi soittolista sisältäen samankaltaisia kappaleita.

## Käyttäjät
Sovelluksen käyttäjäroolit ovat normaalikäyttäjä ja moderaattori/admin. 

## Perustoiminnallisuus
* Käyttäjä voi luoda käyttäjätunnuksen
* Käyttäjä voi kirjautua sisään
* Käyttäjä voi valita soittolistan, jonka pohjalta hän haluaa luoda samankaltaisen soittolistan
	* Käyttäjä voi valita, onko soittolista julkinen vai yksityinen
	* Käyttäjä voi luoda nimen uudelle soittolistalle

* Sovellus luo käyttäjän spotify-profiilille uuden soittolistan automaattisesti
* Admin voi halutessaan poistaa käyttäjätunnuksen
## Toteutus
* Sovellus toteutaan hyödyntäen Spotifyn kehittäjäalustalta löytyvää 'Spotify Web API'-rajapintaa 'SpotiPy' kirjaston avulla. 

## Käyttöliittymäluonnos
Käyttöliittymä koostuu neljästä ikkunasta  

![IMG-5813](https://user-images.githubusercontent.com/102043449/160628252-3ad63f15-0c6b-4723-a15c-c39df3b8a05b.jpg)
*Statistiikkaikkuna toteutetaan ainoastaan, jos aikaa jää tarpeeksi*

## Jatkokehitysideoita
* Käyttäjä voi vaihtoehtoisesti valita olemassaolevan soittolistan sijasta genren, jonka pohjalta uusi soittolista generoidaan.
* Sovellus näyttää statistiikkoja luoduista soittolistoista:
	* Suosituimmat genret
	* Suosituimmat artistit
	* Suosituimmat albumit
