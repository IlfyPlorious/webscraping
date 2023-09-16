Autor:

Sandu Dragos Florian
0732209414
sdragosflorian@gmail.com

Instructiuni:

Instalarea dependintelor:

Pentru functionarea aplicatiei este necesar ca pe sistemul utilizatorului sa fie 
instalat Python3
De asemenea trebuie instalat browserul Google Chrome
Daca nu se doreste instalarea browserului Google Chrome,
a se vedea liniile 30-40 din main.py

linux: sudo apt-get install python3
windows: instalarea python3 prin descarcarea de pe un browser web

Apoi, cu ajutorul comenzii pip, vor fi necesare urmatoarele module:
pip install beautifulsoup4
pip install selenium
pip install webdriver_manager
pip install pymongo
pip install dnspython
pip install lxml


Pentru rularea aplicatiei:

Se deschide un terminal bash pentru linux sau powershell pentru windows
Se navigheaza pana in directorul eMagScraping

sau
linux: python3 full/path/to/main.py
(sau deschiderea consolei in folderul proiectului si rularea comenzii
python3 main.py)
windows: pentru a rula python full/path/to/main.py
este necesara adaugarea la PATH a executorului python

Aplicatia deruleaza interactiunea cu utilizatorul folosind consola.

Pentru a testa functionarea unor featureruri extra care nu functioneaza consistent, a se vedea 
comentariile de pe linia 64 din main.py:
# urmatoarele secvente comentate efectueaza parcurgerea spre a 2 a pagina
    # pe sistemul meu - laptop linux, codul functioneaza fara probleme
    # insa pe windows, am intampinat mai multe probleme. Daca dimensiunea ecranului sistemului este
    # mai mica de 1980 x 1080, chiar daca am setat dimensiunea ferestrei sa fie aceasta,
    # butonul de pagina este dedesubtul butonului de cookies, insa acesta nu functioneaza.
    # astfel nu poate am reusit sa realizez o solutie consistenta pentru a accesa a doua pagina


