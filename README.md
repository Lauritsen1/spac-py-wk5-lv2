Mit projekt er et lagerstyringssystem bygget i Python. Her er en kort beskrivelse af, hvordan det fungerer:

- **Produktoprettelse**: Til oprettelse af produkter har jeg brugt factory pattern, hvor jeg har lavet specifikke produktklasser ud fra en abstrakt produktklasse.
  `ProductFactory` klassen tager imod input og matcher inputtet til det rigtige produkt og laver en instans.
- **Database**: Produktinformation sendes til en SQLite database, håndteret af `Connection` klassen, som sikrer kun én aktiv forbindelse ved hjælp af singleton pattern.
- **Inventory**: Produkterne tilføjes til et `Inventory` objekt, der kan vise produkterne samlet eller filtreret efter kategori.

For at starte projektet, følg disse trin:

1. Åbn en terminal og naviger til projektets root.
2. Opret en virtuel Python-miljø ved at køre `python -m venv .venv`
3. Aktiver det virtuelle miljø ved at køre `.venv\Scripts\activate`
4. Installer de nødvendige pakker ved at køre `pip install -r requirements.txt`
5. Start programmet ved at køre `python main.py`
