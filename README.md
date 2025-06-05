# Eigener Sprachassistent

Dieses Projekt demonstriert einen einfachen Sprachassistenten auf Basis der OpenAI API. 
Er nimmt Sprache vom Mikrofon auf, sendet den Text an ChatGPT und gibt die Antwort 
per Text-to-Speech wieder. Der Assistent spricht deutsch und verhält sich im Stil von 
Bender aus der Serie *Futurama*.

## Voraussetzungen

* Python 3.9 oder neuer
* Ein Mikrofon an Ihrem Raspberry Pi
* Installierte Pakete aus `requirements.txt`
* Eine Umgebungsvariable `OPENAI_API_KEY` mit Ihrem OpenAI-Schlüssel

Pakete installieren:
```bash
pip install -r requirements.txt
```

## Starten

```bash
python assistant.py
```

Nach dem Start wartet der Assistent auf Spracheingaben. Jede erkannte Aussage wird an 
die OpenAI API geschickt und anschließend als Sprachausgabe wiedergegeben. Der Stil der 
Antwort orientiert sich an Bender.

