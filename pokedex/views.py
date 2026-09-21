from django.shortcuts import render

from .data import POKEMON_DATA


def index(request):
    """Muestra las tablas con los datos de los Pokémon."""
    pokemones = []
    for pokemon in POKEMON_DATA:
        pokemones.append({
            'nombre': pokemon['nombre'],
            'id_formateado': str(pokemon['id']).zfill(3),
            'tipo1': pokemon['tipo1'],
            'tipo2': pokemon['tipo2'] or '-',
            'estadisticas': pokemon['estadisticas'],
        })

    contexto = {'pokemones': pokemones}
    return render(request, 'pokedex/index.html', contexto)
