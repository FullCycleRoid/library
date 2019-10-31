from catalog.geodata import geodata


def base_context_visits(request):
    return {'geodata': geodata(request)}


