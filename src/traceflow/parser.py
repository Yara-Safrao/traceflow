import os
import sys
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
    """Lê um ficheiro de log, ignora linhas inválidas e marca a origem de cada evento."""
    source = os.path.basename(path)
    events = []
    with open(path) as ficheiro:
        for number, line in enumerate(ficheiro, start=1):
            if not line.strip():
                continue
            try:
                event = parse_line(line)
            except (IndexError, ValueError):
                print(f"Linha {number} ignorada em {source}: {line.strip()}", file=sys.stderr)
                continue
            event["source"] = source
            events.append(event)
    return events