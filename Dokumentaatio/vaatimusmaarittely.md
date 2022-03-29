#Vaatimusmäärittely
##Sovelluksen idea
Sovelluksen käyttäjä voi valita spotify kirjastostaan soittolistan, jonka avulla käyttäjälle luodaan uusi soittolista sisältäen samankaltaisia kappaleita.

##Käyttäjät
Sovelluksen ainoa käyttäjärooli on normaali käyttäjä.

##Perustoiminnallisuus
* Käyttäjä voi valita soittolistan, jonka pohjalta hän haluaa luoda samankaltaisen soittolistan
	* Käyttäjä voi valita, onko soittolista julkinen vai yksityinen
	* Käyttäjä voi luoda nimen uudelle soittolistalle

* Sovellus luo käyttäjän spotify-profiilille uuden soittolistan automaattisesti

##Toteutus
* Sovellus toteutaan hyödyntäen Spotifyn kehittäjäalustalta löytyvää 'Spotify Web API'-rajapintaa 'SpotiPy' kirjaston avulla. 

##Jatkokehitysideoita
* Käyttäjä voi vaihtoehtoisesti valita olemassaolevan soittolistan sijasta genren, jonka pohjalta uusi soittolista generoidaan.
* Sovellus näyttää statistiikkoja luoduista soittolistoista:
	* Suosituimmat genret
	* Suosituimmat artistit
	* Suosituimmat albumit
