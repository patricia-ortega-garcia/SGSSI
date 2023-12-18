# TOR (The Onion Router)


https://community.torproject.org
https://community.torproject.org/es/onion-services/
https://community.torproject.org/onion-services/overview/

## TOR browser

https://www.torproject.org/download/
Descomprimir
Ejecutar: [mikel@Durruti tor-browser]$ ./start-tor-browser.desktop

Conectarse a la red Onion
Sitios ONION: https://community.torproject.org/es/onion-services/, por ejemplo https://www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion/

PREGUNTA: por que entre los sitios Onion hay tantos periodicos?

https://www.globaleaks.org/

## TOR server en Google Cloud

Arrancar servidor en Google Cloud

### Instalar TOR

https://community.torproject.org/onion-services/setup/install/

TOR tiene sus propios repos Debian: https://support.torproject.org/apt/tor-deb-repo/

$ dpkg --print-architecture
$ sudo apt update
$ sudo apt install apt-transport-https
$ sudo vim /etc/apt/sources.list.d/tor.list
	$ lsb_release -c
$ sudo -s
$ wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | tee /usr/share/keyrings/tor-archive-keyring.gpg >/dev/null

O meter el sudo en gpg (https://ubuntuforums.org/showthread.php?t=2473314):

$ wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | sudo gpg --dearmor | sudo tee /usr/share/keyrings/tor-archive-keyring.gpg >/dev/null
$ sudo apt update
$ apt install tor deb.torproject.org-keyring

Verificar (https://tor.stackexchange.com/questions/12678/how-to-check-if-tor-is-working-and-debug-the-problem-on-cli):
$ curl -x socks5h://localhost:9050 -s https://check.torproject.org/api/ip
$ {"IsTor":true,"IP":"185.220.101.26"}

### Configurar servidor Onion

https://community.torproject.org/onion-services/setup/

Apache funcionando, puerto 80 abierto

sudo vim /var/www/html/index-onion.html
http://34.66.152.194/index-onion.html


sudo vim /etc/tor/torrc

HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:80


sudo systemctl restart tor

sudo less /var/lib/tor/hidden_service/hostname

TOR browser: http://q245tai5x7pkr5vmzxnfm2bu4bmc6ip4u6qajncr5hlx2gjrdwr2u6yd.onion/index-onion.html



