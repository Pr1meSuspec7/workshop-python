# Workshop Python

In questo workshop vedremo in azione Python e alcuni casi d'uso.<br>
Vedremo come automatizzare la configurazione degli apparati network usando le API.

Per poter utilizzare il materiale di questo corso avrete bisogno di:
*  Python 3.x + modulo virtualenv
*  Configurazione di un virtual environment python

## Istruzioni
Utilizzate i seguenti comandi per configurare il vostro ambiente python:<br>
* installare python dal seguente link: https://www.python.org/downloads/<br>
* scaricate nella vostra HOME il repository in formato .zip<br>
* scompattate il file .zip nella vostra HOME, poi entrate nella cartella "workshop-python"<br>
`$ cd workshop-python`<br>
* installare modulo virtualenv
`$ pip install virtualenv`<br>

*  creare virtualenv<br>
`$ python3 -m venv venv-workshop-python`<br>
*  attivare virtualenv<br>
```
Lunux:
$ source venv-workshop-python/bin/activate
```
```
Windows CMD:
C:\> venv-workshop-python\Scripts\activate.bat
```
```
Windows PowerShell:
PS C:\> venv-workshop-python\Scripts\Activate.ps1
```
<br>

Sul prompt dovrebbe apparire il nome del virtualenv:<br>
`(venv-workshop-python) $ `

* verificare installazione di Python<br>
`$ python -V`<br>
`Python 3.13.0`<br>
