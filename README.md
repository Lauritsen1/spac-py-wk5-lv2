Til selve produkt oprettelse bruger jeg factory pattern, hvor jeg har lavet specifike produkt klasser ud fra en abstract produkt klasse,
ProductFactory klassen tager imod input og matacher så inputtet til det rigtige produkt og laver en instance, hvor efter produkt info bliver sendt til en SQLite database, 
håndteret af Connection klassen, som sikrer kun én aktiv forbindelse ved hjælp af singleton pattern. 
Produkterne tilføjes til et Inventory objekt, der kan vise produkterne samlet eller filtreret efter kategori.

For at starte dit projekt, følg disse trin:

Åbn en terminal og naviger til projektets root.
Opret en virtuel Python-miljø ved at køre "python -m venv .venv"
Aktiver det virtuelle miljø ved at køre ".venv\Scripts\activate"
Installer de nødvendige pakker ved at køre "pip install -r requirements.txt"
Start programmet ved at køre "python main.py"
