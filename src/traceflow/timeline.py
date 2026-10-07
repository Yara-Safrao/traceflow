from .parser import read_log


def sort_events(events):
    """Devolve os eventos ordenados do mais antigo para o mais recente."""
    return sorted(events, key=lambda evento: evento["timestamp"])


def merge_logs(paths):
    """Lê vários ficheiros e junta tudo numa só linha temporal."""
    todos = []
    for path in paths:
        todos.extend(read_log(path))
    return sort_events(todos)