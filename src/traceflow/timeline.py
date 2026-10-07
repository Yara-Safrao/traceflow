def sort_events(events):
    """Devolve os eventos ordenados do mais antigo para o mais recente."""
    return sorted(events, key=lambda evento: evento["timestamp"])