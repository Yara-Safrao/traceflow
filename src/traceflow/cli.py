import argparse

from .detector import find_bruteforce
from .timeline import merge_logs


def main():
    parser = argparse.ArgumentParser(description="Análise cronológica de logs.")
    parser.add_argument("logs", nargs="+", help="ficheiros de log a juntar")
    parser.add_argument("--threshold", type=int, default=3,
                        help="falhas seguidas antes de um sucesso para gerar alerta")
    args = parser.parse_args()

    events = merge_logs(args.logs)

    print("== Timeline ==")
    for e in events:
        print(f"{e['timestamp']}  [{e['source']}]  {e['level']}  {e['message']}")

    alerts = find_bruteforce(events, args.threshold)
    print("\n== Alerts ==")
    if not alerts:
        print("Nenhum padrão suspeito encontrado.")
    for a in alerts:
        print(f"{a['timestamp']}  {a['failures']} falhas seguidas e depois sucesso, IP {a['ip']}")


if __name__ == "__main__":
    main()