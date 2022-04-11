Autor:

Sandu Dragos Florian
0732209414
sdragosflorian@gmail.com

Instructiuni:

Instalarea dependintelor:

Pentru functionarea aplicatiei este necesar ca pe sistemul utilizatorului sa fie 
instalat Python3
De asemenea trebuie instalat browserul Google Chrome

linux: sudo apt-get install python3
windows: instalarea python3 prin descarcarea de pe un browser web

Apoi, cu ajutorul comenzii pip, vor fi necesare urmatoarele module:
pip install beautifulsoup4
pip install selenium
pip install webdriver_manager
pip install pymongo
pip install dnspython


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

