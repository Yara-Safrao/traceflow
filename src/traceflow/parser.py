from datetime import datetime


def parse_line(line):
    """Transforma uma linha de log num dicionário com data, nível e mensagem."""
    partes = line.strip().split(" ", 3)
    data_texto = partes[0] + " " + partes[1]
    return {
        "timestamp": datetime.strptime(data_texto, "%Y-%m-%d %H:%M:%S"),
        "level": partes[2],
        "message": partes[3],
    }


def read_log(path):
    """Lê um ficheiro de log e devolve uma lista de eventos."""
    events = []
    with open(path) as ficheiro:
        for line in ficheiro:
            if line.strip():
                events.append(parse_line(line))
    return events