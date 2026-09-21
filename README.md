# Proyecto2 - Pokédex (Django)

Proyecto Django que muestra 10 tablas con datos y estadísticas de Pokémon
(Nombre, ID, Tipo 1, Tipo 2, Vida, Ataque, Defensa, Ataque especial,
Defensa especial y Velocidad).

## Cómo correrlo

1. Crea y activa un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS / Linux
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Aplica las migraciones (crea la base de datos sqlite, aunque este
   proyecto no usa modelos todavía):
   ```
   python manage.py migrate
   ```

4. Corre el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

5. Abre tu navegador en http://127.0.0.1:8000/

## Editar los Pokémon mostrados

Los datos están en `pokedex/data.py`, en la lista `POKEMON_DATA`. Puedes
agregar, quitar o modificar Pokémon ahí; cada uno es un diccionario con
`nombre`, `id`, `tipo1`, `tipo2` (usa `None` si no tiene) y `estadisticas`.

