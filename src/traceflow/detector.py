import re


def get_ip(message):
    """Extrai o endereço IP de uma mensagem (ip=...), ou None."""
    match = re.search(r"ip=(\S+)", message)
    return match.group(1) if match else None


def find_bruteforce(events, threshold=3):
    """Procura vários logins falhados seguidos de um sucesso, do mesmo IP."""
    failures = {}
    alerts = []
    for event in events:
        ip = get_ip(event["message"])
        if ip is None:
            continue
        if "login failed" in event["message"]:
            failures[ip] = failures.get(ip, 0) + 1
        elif "login success" in event["message"]:
            if failures.get(ip, 0) >= threshold:
                alerts.append({
                    "timestamp": event["timestamp"],
                    "ip": ip,
                    "failures": failures[ip],
                })
            failures[ip] = 0
    return alerts